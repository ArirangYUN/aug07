#학업성적_클래스.py

import DBModule 

class Score:
    def __init__(self):
        self.db = DBModule.DBModule()  

    def append(self):
        name = input("이름 : ")
        kor = input("국어 : ")
        eng = input("영어 : ")
        mat = input("수학 : ")
        
        sql = """
        insert into score(name, kor, eng,mat)
        values(%s, %s, %s, %s)
        """
        self.db.execute(sql, (name, kor, eng, mat))
    
    def output(self):
        sql = """
        select id, name, kor, eng, mat, 
        kor+eng+mat as total,
        (kor+eng+mat)/3 as avg 
        from score
        """
        result = self.db.executeAll(sql)
        i = 1
        for row in result:
            print(i, end='\t')
            #print(row['id'], end='\t')
            print(row['name'], end='\t')
            print(row['kor'], end='\t')
            print(row['eng'], end='\t')
            print(row['mat'], end='\t')
            print(row['total'], end='\t')
            print(row['avg'])
            i=i+1
            



#__name__ - 모든 파이썬 파일에 자동으로 붙는 변수 
#           자기파일명, 이 파일로 직접 프로그램을 수행하면 
#           __main__으로  오고, 만일 모듈로 작동된다면 
#           자기 파일명이 전달된다 

if __name__ == "__main__":
    score = Score() 
    #score.append()
    score.output()


