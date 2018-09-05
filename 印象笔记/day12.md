---
title: day 12
tags: 
notebook: 数据库
---
1. unique 唯一约束
   primary key 主键约束
   foreign key外键约束
   非空约束 not null 与 默认值 default
 
```SQL
create table student_score(
    id int  primary key  not null auto_increment comment '序号',
    stu_id  int not null comment '学号',
    teacher varchar(10) not null comment '代课老师',
    course varchar(10) not null comment '课程',
    exam_date date not null comment '考试时间',
    score int(3) not null comment '成绩',
    foreign key(stu_id) references students(stu_id)) comment '学生成绩' ;
alter table score_db_1_20180713 add constraint fk_stu_id
```
2. select * from scores where stu_id in (select stu_id from scores where score < 60);
3. select * from scores where stu_id in (select stu_id from scores where score < 30);
4. select * from scores as p1 join scores as p2 on p1.stu_id = p2.stu_id and p2.score < 30 ;
5. select students.stu_id,name,score,teacher,exam_date from students inner join scores on students.stu_id = scores.stu_id;
6. select students.stu_id,name,score,teacher,exam_date from students,scores where students.stu_id = scores.stu_id;
7. select name,age,score from students as s join scores as c on s.stu_id = c.stu_id ;
8. select id,stu_id,score from scores where stu_id = (select stu_id from scores where id =2);
9. select p1.id,p1.stu_id,p1.score from scores as p1 join scores as p2 on p1.stu_id = p2.stu_id and p2.id=2;
10. select p1.name,p2.score from students as p1 inner join scores as p2 on p1.stu_id = p2.stu_id;
11. select p1.name,p2.score from students as p1 left OUTER join scores as p2 on p1.stu_id = p2.stu_id and p2.score >=60 ;
12. select p1.stu_id,p1.name,count(p2.score) from students as p1 inner join scores as p2 on p1.stu_id = p2.stu_id and p2.score >=60 GROUP BY p1.stu_id HAVING count(p2.score) =3 ;




# linux
1. cat /proc/cpuinfo  | grep processor 查看线程


```python
import mysql.connector as c
from faker import Faker
import random
import os
from multiprocessing import Pool

conn = c.connect(user='root', password=os.getenv("p"), database='stu_220')
cursor = conn.cursor()
fake = Faker("zh_CN")


def get_native_place(address: str, key="县市") -> str:
    return [address[:address.index(k) + 1] for k in key if k in address][0]


def gen_stu_obj():
    address = fake.address()
    native_place = get_native_place(address)
    birthday = fake.date_of_birth(tzinfo=None, minimum_age=2, maximum_age=85)
    email = fake.ascii_free_email()
    name = fake.name()
    phone = fake.phone_number()
    id_type = "身份证"
    age = random.randint(2, 80)
    id_code = fake.ssn(min_age=20, max_age=25)
    abbr_name = fake.romanized_name()[:4]
    enrollment_time = fake.date_between(start_date="-2y", end_date="today")
    hobby = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    sex = random.choice(["男", "女"])
    stu_id = None
    return locals()


def insert_to_db(data: dict, table: str):
    placeholder = ", ".join(["%s"] * len(data))
    stmt = "insert into `{table}` ({columns}) values ({values});".format(table=table,
                                                                         columns=",".join(data.keys()),
                                                                         values=placeholder)
    cursor.execute(stmt, list(data.values()))
    conn.commit()


if __name__ == "__main__":
    import sys
    if len(sys.argv) <= 1:
        raise Exception("必须给我一个参数")
    else:
        count = sys.argv[1]
    import time

    start = time.time()
    pool = Pool(4)
    for _ in range(int(count)):
        data = gen_stu_obj()
        pool.apply_async(insert_to_db,(data,"students_fake",))
    pool.close()
    pool.join()
    print(time.time() - start)```
