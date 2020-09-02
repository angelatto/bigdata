# bigdata
2019-2학기 빅데이터처리 수업 

[hw2]
주제 : 엑셀로 학점을 매기는 프로그램 만들기
조건 : total 점수는 midterm 30%, final 35%, hw34%, attendance 1% 로 구성된다.
(midterm, final, hw는 100점 만점, attendance는 1점 만점)
학점 부여 규칙은 다음과 같다.
- 학점은 A+,A0,B+,B0,C+,C0,F중의 하나로 부여한다.
- A는 학생수의 30%를 넘지 않도록 부여하며 A학점을 가능한 최대로 부여한다.
- A+는 A 학점에서 최대 50%를 넘지 않으며 A+도 가능한 최대로 부여한다.  - A와 B는 학생 수의 70%를 넘지 않도록 부여하며 가능한 최대로 부여한다.
- B+는 B학점에서 최대 50%를 넘지 않으며 B+도 가능한 최대로 부여한다. - 나머지 학생들은 C를 부여한다.
- C+는 C 학점에서 최대 50%를 넘지 않으며 가능한 최대로 부여한다. - 총점이 40점 미만이면 위 규칙과 상관없이 F학점을 부여한다.

실행 방법 : python3 student20170971.py, (엑셀 파일은 student.xlsx 이용)


[hw3]
주제 : How can we access the IMDb data?
We need know how many movies falls into each genre.
Input file : movie.dat -> Output : <Genre> <# of movies>

실행 방법 : python3 IMDBStudent20170971.py <movie.dat> <movieoutput.txt>


[hw4-1]
주제 : How can we access the price data? We can get price data via http requests. 
Then, we can put the data into the database. 
Write the python code that retreives price data and stores the data into the datbase every 10 minutes.

실행 방법 : python3 HW4_1_Student20170971.py config.props



[hw4-2]
주제 : Write python program that can show today's price trend of cyptocurrency through the web.
Ex) http://localhost:8080/BTC/KRW

실행 방법 : python3 HW4_2_Student20170971.py config.props



[hw5]
주제 : k-Nearest Neighbor 알고리즘을 이용해서 필기체 인식 시스템을 만들기 

실행 방법 : python3 Student20170971.py <트레이닝 데이터 폴더> <학습 데이터 폴더>
