---
title: day5
tags: 
notebook: 数据库
---
# Python
1. uuid 

# 数据库
1. insert into 

~~insert into custmers values(null,'田真','123@gmail.com','河南','122312','1992-10-5');~~ 
insert into custmers(id,name,email,address,phone,birthday) values(null,'田真','123@gmail.com','河南','13213','1992-10-5')

2. 多行插入
insert into custmers(name,phone) values ('张三','123'),('李四','234');
3. 重定向
```SQL
insert into new_custmer(name,phone) select name,phone from custmers;
```
4. 更新
update custmers set email = '123@163.com' where id = 12 修改12号的邮箱地址
select * from student where name like '刘%' 寻找以刘开头的所有人
select * from student where name like '%刘' 寻找以刘结尾的所有人
5. badboy表
```SQL
create table badboy(
    id int auto_increment comment '学号',
    name varchar(50) not null comment '姓名',
    age int not null comment '年龄',
    place varchar(50) not null comment '籍贯',
    primary key(id))comment '男孩';

insert into badboy  select  id,name,age,place from student where sex 
= '男';
```
把student表中的id,name,age,place 导入badboy表中.

6. 删除行
delete from badboy where id = 1504762; 删除id=1504762这一行
select count(*) from badboy;
