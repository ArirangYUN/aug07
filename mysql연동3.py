import pymysql
#1. 연결 객체 만들기 
conn = pymysql.connect(host="localhost", #디비서버아이피
        user='root',
        password='1234',
        db='mydb',
        charset='utf8',
        port = 5306
)

#2. 커서객체 만들기 
cursor = conn.cursor(pymysql.cursors.DictCursor)

#트랜잭션 상태

number = input("사원번호 : ")
name = input("사원이름 : ")

# sql = "insert into emp (empno, ename) values( " + str(number) + 
#      ", '" + name + "') "
#insert into emp (empno, ename) values( 111, 'ㅇㅇㅇ')

sql = "insert into emp (empno, ename) values({} '{}')".format(number,name)
cursor.execute(sql)

#파라미터 사용기법 
sql = """
    insert into emp(empno, ename) 
    values(%s, %s) 
""" 
#변수들을 튜플로 전달하면%s 위치에 알아서 자동으로 전달 
cursor.execute(sql, (number, name))

conn.commit() #수정내용확정 

conn.close()
