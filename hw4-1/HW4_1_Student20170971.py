import urllib.request, urllib.parse, urllib.error
import sqlite3
import datetime
import time
import sys
import configuration
from ast import literal_eval

def get_connection(configProps):
    try:
        conn = sqlite3.connect(configProps['DB.db'])
        return conn
    finally:
        pass

def initdb(con):
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS PRICE_TBL")
    cursor.execute("CREATE TABLE PRICE_TBL(CurrentTime VARCHAR(20) NOT NULL, CryptoCurrencyName varchar(10) NOT NULL, TargetCurrencyName VARCHAR(10) NOT NULL,Price DECIMAL(20,5) NOT NULL)")
    cursor.close()


def insertDB(ctime, cname, tname, price, con):
    cursor = con.cursor()
    cursor.execute("INSERT INTO PRICE_TBL VALUES (\'%s\', \'%s\', \'%s\', %0.5f)" % (ctime, cname, tname, price))
    con.commit();
    cursor.close()


if __name__ == "__main__":
    config = str(sys.argv[1])
    db_c = configuration.get_db_configuration(config)
    
    db_conn = get_connection(db_c)
    initdb(db_conn)
    db_conn.commit()
    
    
    while(1):
        now = datetime.datetime.now()
        clock = "%d-%d-%d %d:%d:%d" % (now.year,now.month,now.day,now.hour,now.minute,now.second)

        
        Bhand = urllib.request.urlopen('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,KRW')

        for line in Bhand:
            rst = line.decode().strip()
            rst = str(rst)
            dic = literal_eval(rst)          
            insertDB(clock, 'BTC', 'USD', dic['USD'] ,db_conn)
            insertDB(clock, 'BTC', 'JPY', dic['JPY'] ,db_conn)
            insertDB(clock, 'BTC', 'EUR', dic['EUR'] ,db_conn)
            insertDB(clock, 'BTC', 'KRW', dic['KRW'] ,db_conn)
           
        now = datetime.datetime.now()
        clock = "%d-%d-%d %d:%d:%d" % (now.year,now.month,now.day,now.hour,now.minute,now.second)


        Ehand = urllib.request.urlopen('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,JPY,EUR,KRW')

        for line in Ehand:
            rst = line.decode().strip()
            rst = str(rst)
            dic = literal_eval(rst)          
            insertDB(clock, 'ETH', 'USD', dic['USD'] ,db_conn)
            insertDB(clock, 'ETH', 'JPY', dic['JPY'] ,db_conn)
            insertDB(clock, 'ETH', 'EUR', dic['EUR'] ,db_conn)
            insertDB(clock, 'ETH', 'KRW', dic['KRW'] ,db_conn)
        
        time.sleep(600)
        
    db_conn.close()
