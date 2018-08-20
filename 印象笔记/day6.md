---
title: day 6
tags: 
notebook: 数据库
---
# 数据库
### 去重
1. ```select distinct age from students;```
从学生表中找出所有年龄并且去重
2. ``` select distinct age from students order by age;```
按年龄排序去重
3. ```select count(*),age from students group by age;```
### limit
查找出每个年龄段有多少学生
1. ```select * from badboy  limit 5;```
显示前五行
2. ```select * from badboy  limit 5,10;```
从第五行开始到查看10行
3. ```select * from badboy limit 4 offset 3;select * from badboy limit 3,4```从第三行开始取4个
### order by 
1. ```select name,age from students order by age ; ```
按年龄排序
2. ```select name,age from students order by age  desc; ```
按年龄倒叙
3. ```select name,age from students order by age  desc limit 1 ;```
找出年龄最大的人
```update  students set age = 19 where year(birthday) = 2000;``` 
4. 修改2000年的年龄
```select id,name from students order by age,name ;```
先按年龄在按名字
### desc asc  
desc 是descend 降序意思
asc 是ascend 升序的意思     
### count ,between and ,or , in ,not 
1. ```select age,name from students where age between 19 and 20;```
2. ```select count(*) as c,left(name,1) from students group by left(name,1) order by c desc ; ```
统计姓氏数量并且排序
```select name from students where left(first_name,1) between 'a' and 'f';```
寻找姓a-f之间的所有名字
3. 正则表达式查找
```select name from students where first_name regexp '^[a-z]';```
4. ```select * from students where email is not null;```
5. ```select length(first_name),count(*) from students group by length(first_name);```
按名字字数分类统计个数
6. ```select name from students where age = 23 or sex = '女'```;
查找年龄是23或者是女性的
7. ```select name from students where age = 23 or sex = '女';select name from syudents where age between 19 and 20;select name from syudents where age in (19,20);```
8.  ```select name from syudents where age not in (19,20);``` 
查询不是19,20
# python 
1. ```__doc__``` 查看函数的说明,注释