import sys
import datetime

input = sys.argv[1]
output = sys.argv[2]

def getDayName(m, d, y):
    dayString = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return dayString[datetime.date(int(y),int(m), int(d)).weekday()]

try:
    f1 = open(input, "rt")
    result = dict()  #output파일에 출력할 딕셔너리 생성
    text = f1.read()  
    uberList = text.splitlines()
    
    for line in uberList: #파일에서 한줄 의미 
        uber = line.split(",")
        dList = uber[1].split("/")
        dName = getDayName(dList[0], dList[1], dList[2]) #요일
        key = uber[0]+ "," + dName
        if key not in result:
            value = uber[2] + "," + uber[3]            
            result[key] = value
        else:
            v = result[key].split(",")
            v[0] = int(v[0]) + int(uber[2])
            v[1] = int(v[1]) + int(uber[3])
            value = str(v[0]) + "," + str(v[1])
            result[key] = value

    f2 = open(output, "wt")
    for i in result:
        newinput = i + " " + result[i] + "\n"
        f2.write(newinput)        

except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f1.close()
    f2.close()
