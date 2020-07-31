import sys

input = sys.argv[1]
output = sys.argv[2]

try:
    f1 = open(input, "rt")
    result = dict() #output파일에 출력할 딕셔너리 생성
    text = f1.read()
    movieList = text.splitlines()
    for line in movieList: #line은 파일의 한 줄 의미
        movie  = line.split("::")
        genreList = movie[2].split("|")    
        for g in genreList: #장르가 이미 있으면 +1, 없다면 새로 추가 =1
            if g not in result:
                result[g] = 1
            else:
                result[g] += 1 
    f2 = open(output, "wt")
    for i in result:
        newinput = i + " " + str(result[i]) + "\n"
        f2.write(newinput)
except FileNotFoundError:    
    print("파일이 없습니다.")
finally:
        f1.close()
        f2.close()

