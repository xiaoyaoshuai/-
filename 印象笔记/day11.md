---
title: day 11
tags: 
notebook: 数据库
---
```SQL
create table student_score(
    id int auto_increment not null comment '序号',
    stu_id  int not null comment '学号',
    teacher varchar(10) not null comment '代课老师',
    course varchar(10) not null comment '课程',
    exam_date date not null comment '考试时间',
    score int(3) not null comment '成绩',
    primary key(id)) comment '学生成绩' ;
```
```python
import pandas as pd
import mysql.connector as c
db = c.connect(user='root', passwd='abcd1234', database='stu_220', host='192.168.4.14')
cursor = db.cursor()
s = pd.read_excel('/home/ws/Downloads/第一、二周考成绩.xlsx')
info_dict = s.T.to_dict()
for k,v in info_dict.items():
    id = v['序号']
    stu_id = v['学号']
    teacher = v['代课老师']
    course = v['课程']
    exam_date = str(v['考试时间'])
    score = v['成绩']
    sql ="""insert into student_score(id,teacher,course,exam_date,score) values(%s,%s,%s,%s,%s)"""
    cursor.execute(sql,(stu_id,name,teacher,course,exam_date,score_week1,score_week2))
db.commit()
```

1. select name from students 
   where stu_id in 
   ( select DISTINCT(stu_id) 
   from scores where score < 60);
2. select COUNT(*) as c,stu_id from 
   scores where score < 60 
   GROUP BY stu_id HAVING c = 2;
3. select name from students 
   where stu_id in 
   (select stu_id from scores 
   where score < 60 
   GROUP BY stu_id 
   HAVING count(*) = 2) ;
4. select students.stu_id,name,phone,native_place,score,exam_date,course 
   from students join student_score 
   on students.stu_id = student_score.stu_id;

# python

字典　集合　列表　　推导式
re模块　match,search findall compile

