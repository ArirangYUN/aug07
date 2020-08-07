#mysql연동1.py

#1.라이브러리 불러오기 
import pymysql

#2. db와 연결하여연결객체를 만든다 

try:

    #mysql 기본포트는 3306, 만일 포트를 바꾸면 포트값을 전달해야한다
    conn = pymysql.connect(host="localhost", #디비서버아이피
            user='root',
            password='1234',
            db='mydb',
            charset='utf8',
            port = 5306
    )

    #커서를 만든다.  커서를  통해서 디비데이터를 읽고 쓸 수 있다
    sql = "select empno, ename, job, sal from emp"
    cursor = conn.cursor(pymysql.cursors.DictCursor) # 커넥션객체를 통해 커서를 얻는다 

    cursor.execute(sql) 
    # sql을 실행시키고 그 결과는 내부적으로  커서가 가지고 있다. 
    #커서로부터 데이타셋을 가져온다 
    #데이터를 tuple타입으로 가져온다 
    rows = cursor.fetchall()
    for row in rows:
        #print(row)
        print(row['ename'], row['sal'])
    conn.close() #연결닫기

except Exception as e:
    print(e.args[0])



#mysql python cursor dict
#https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursordict.html


