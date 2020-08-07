import pymysql
#1. 연결 객체 만들기 
conn = pymysql.connect(host="localhost", #디비서버아이피
        user='root',
        password='1234',
        db='mydb',
        charset='utf8',
        port = 5306
)

def append():
    name = input("이름 : ")
    kor = input("국어 : " )
    eng = input("영어 : ")
    mat = input("수학 : ")
    sql = """ insert into score(name, kor, eng, mat)
            values(%s, %s, %s, %s)
            """
    cur = conn.cursor()
    cur.execute(sql, (name, kor, eng, mat))
    conn.commit()

def output():
    sql = """
    select name, kor, eng, mat, kor+eng+mat total 
    from score
    """ 
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute(sql)
    rows = cur.fetchall()

    """
     Ctrl+Shift+X
     ctrl+shifr+Y 
    """
    for row in rows:
        print(row)
        print(row['name'], row['kor'], row['eng'], row['mat'],
        row['total'])

    
    
#append()
output()
