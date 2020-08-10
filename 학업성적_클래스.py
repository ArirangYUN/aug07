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
            
    def search(self):
        key = input("찾을 이름 : ")
        sql = """
            select id, name, kor, eng, mat, 
            kor+eng+mat as total,
            (kor+eng+mat)/3 as avg 
            from score 
            where name like %s
        """
        key = '%' + key + '%'   #백 -> '%백%' 
        result = self.db.executeAll(sql, ( key ) )
        for row in result:
            print(row['id'], end='\t')
            print(row['name'], end='\t')
            print(row['kor'], end='\t')
            print(row['eng'], end='\t')
            print(row['mat'], end='\t')
            print(row['total'], end='\t')
            print(row['avg'])
        
        return len(result) #검색한 데이터 개수를 반환하자 

    def menu(self):
        print("1.전체보기")
        print("2.추가")
        print("3.수정")
        print("4.삭제")
        print("5.검색")
        print("0.종료")
        
    def start(self):
        while(True): #무한루프  - 무한히 한복한다 
            self.menu()
            sel = input("선택 : ")
            if sel =="1":
                self.output()
            elif sel=="2":
                self.append()
            elif sel=="3":
                self.modify()
            elif sel=="4":
                self.delete()
            elif sel=="5":
                self.search()
            elif sel=="0":
                print("프로그램을 종료합니다")
                return #함수를 종료한다 
            else:
                print("선택메뉴가 없습니다. 잘 선택하십시요") 

    def modify(self):
        cnt = self.search()
        if cnt == 0:
            print("검색한 항목이 없습니다.")
            return 

        print("수정할 항목의 아이디를 입력하세요")
        id = input("아이디 : ")
        sql = """ 
        select * from score
        where id=%s 
        """
        result = self.db.executeAll(sql, (id))
        if len(result) !=0:
            name = input("이름 : ")
            kor = input("국어 : ")
            eng = input("영어 : ")
            mat = input("수학 : ")
            sql = """
                update score set name=%s, kor=%s
                , eng=%s, mat=%s 
                where id=%s 
                """
            self.db.execute(sql, (name, kor, eng, mat, id))
            print("수정되었습니다")

    def delete(self):
        cnt = self.search()
        if cnt == 0:
            print("검색한 항목이 없습니다.")
            return 

        print("삭제할 항목의 아이디를 입력하세요")
        id = input("아이디 : ")
        sql = """ 
        delete from score   where id=%s 
        """
        self.db.execute(sql, (id))
        print("삭제되었습니다")


#__name__ - 모든 파이썬 파일에 자동으로 붙는 변수 
#           자기파일명, 이 파일로 직접 프로그램을 수행하면 
#           __main__으로  오고, 만일 모듈로 작동된다면 
#           자기 파일명이 전달된다 

if __name__ == "__main__":
    score = Score() 
    #score.append()
    #score.output()
    #score.search()
    score.start()
