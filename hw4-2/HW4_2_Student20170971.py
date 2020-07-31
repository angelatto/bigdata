import sqlite3
import sys
import configuration
import datetime
from socket import *

def get_connection(configProps):
    try:
        conn = sqlite3.connect(configProps['DB.db'])
        return conn
    finally:
        pass

def findTodayDB():
    now = datetime.datetime.now()
    today = "%d-%d-%d " % (now.year, now.month, now.day) #오늘 날짜 
    return today

def findDB(kind1, kind2, conn):
    return __findDB(kind1, kind2, conn.cursor())

def __findDB(kind1, kind2, cursor): 
    today = findTodayDB()
    cursor.execute("SELECT CurrentTime, Price FROM PRICE_TBL WHERE CryptoCurrencyName = '%s' and TargetCurrencyName = '%s' and CurrentTime LIKE '%s'" % (kind1, kind2, today+'%'))

    result = "" 
    while True:
        record = cursor.fetchone() #튜플
        if record == None:
            break
        recordli = list(record) #리스트 
        result += recordli[0] + "    " +str(recordli[1]) + "<br>"
    cursor.close()
    return result

def parserequest(msg, conn):
    msg = str.strip(msg)
    if msg == '': return None;
    msg = msg.split("\n")[0]
    url = msg.split()[1]
    val = url.split('/')
    if len(val) < 3:
        return None;
    
     #문자열임
    return findDB(val[1], val[2], conn)


if __name__ == "__main__":
    config = str(sys.argv[1])
    c = configuration.get_web_configuration(config)
    db_c = configuration.get_db_configuration(config)
    PORT = int(c['web.port'])
    BUFSIZE = int(c['web.bufsize'])

    db_conn = get_connection(db_c)
   
    listen_sock = socket(AF_INET, SOCK_STREAM)
    listen_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    listen_sock.bind(('', PORT))
    listen_sock.listen(1)

    while (1):
        conn, addr = listen_sock.accept()
        data = conn.recv(BUFSIZE).decode("UTF-8")

        rslt = parserequest(data, db_conn)
        if (rslt == None):
            rslt = "Please check url"
        
        msg = "HTTP/1.1 200 OK\n\n\n"
        msg += "<p>Today's Price Table</p>"
        msg += "<html><body>%s</body></html>" % rslt
        conn.sendall(msg.encode("UTF-8"))
        conn.close()

