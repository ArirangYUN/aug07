학업성적 

use mydb;
create table score (
    id int not null auto_increment primary key,
    name  nvarchar(10),
    kor int,
    eng int,
    mat int
);

이름 : 홍길동
국어 : 90
영어 : 90
수학 : 100

디비에 저장하고 디비에 있는 거 전부 출력
홍길동  90 90 100  280  



