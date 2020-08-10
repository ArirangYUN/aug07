import pymysql
import DBModule 

def append():
    name = input("이름 : ")
    kor = input("국어 : " )
    eng = input("영어 : ")
    mat = input("수학 : ")
    sql = """ insert into score(name, kor, eng, mat)
            values(%s, %s, %s, %s)
            """
    db = DBModule.DBModule()
    db.execute(sql, (name, kor, eng, mat))

def output():
    sql = """
        select name, kor, eng, mat, kor+eng+mat as total
        from score 
     """
    db = DBModule.DBModule()
    result = db.executeAll(sql)
    print(result)

output()
#append()

