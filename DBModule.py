#DBModule.py
import pymysql
#1. 연결 객체 만들기 
"""
변수(소문자), 함수(소문자), 상수(전부대문자)
클래스 - 첫글자는 대문자로 그리고 소문자로 쓰다가 새로운 단어시작할때
대문자로 하자
""" 
class DBModule:
    #생성자 - 객체 생성시 자동으로 호출
    #호출자가 시스템일 경우에는 제약사항이 많다.  
    def __init__(self, dbname='mydb'):
        self.conn = pymysql.connect(
                db=dbname,
                charset='utf8',
                host="localhost",  
                user='root',
                password='1234',
                port = 5306
        )
        #pymysql.cursors.DictCursor - 상수 
        #지정안하면 tuple 타입으로 데이터를 가져오므로 
        #dict 타입으로 가져오라고 상수값을 전달 
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def __del__(self):
        self.conn.close()

    def  execute(self, query, args={}):
        self.cursor.execute( query, args)
        self.conn.commit()

    def executeAll(self, query, args={}):
        #특정테이블로 부터 데이터 모두 가져오기
        self.cursor.execute(query, args)
        #쿼리를 실행하고 
        resultset = self.cursor.fetchall()
        # list of dict 한행은 dict  타입, dict 들을 list타입에 담아서 
        # 보냄  
        return  resultset
