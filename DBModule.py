#DBModule.py
import pymysql
#1. 연결 객체 만들기 
class DBModule:
    #생성자 - 객체 생성시 자동으로 호출 
    def __init__(self, dbname='mydb'):
        self.conn = pymysql.connect(
                host="localhost", 
                user='root',
                password='1234',
                db=dbname,
                charset='utf8',
                port = 5306
        )
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def __del__(self):
        self.conn.close()


# db = DBModule()
# sql = """ insert into score(name, kor, eng, mat)
#         values(%s, %s, %s, %s)
#         """
# db.execute(sql, (name, kor, eng, mat))
    
    def  execute(self, query, args={}):
        self.cursor.execute( query, args)
        self.conn.commit()

