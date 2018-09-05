---
title: day16
tags: hd 
notebook: 数据库
---
# 数据库
```SQL
CREATE TABLE bank(
    id int not null auto_increment PRIMARY key COMMENT '序号',
    card char(10) not null COMMENT '卡号',
    name VARCHAR(10) not null COMMENT '姓名',
    money int not null COMMENT '余额');
```
## 事务
1. START TRANSACTION;  开启事务
2. commit 提交数据
3. rollback 撤回
4. 
```sql
START TRANSACTION;
UPDATE bank SEt money = money - 500 where id = 1;
UPDATE bank SEt money = money + 500 where id = 2; 
select * from bank
commit
``` 
5. savepoint + 回滚点名称;
rollback to + 回滚点名称;
show VARIABLES LIKE 'autocommit';显示事务状态
set autocommit = 0;   关闭自动提交
set autocommit = 1;   开启自动提交
6. 锁机制


## 数据备份
/var/lib/mysql  数据库位置
mysqldump -uroot -pabcd12345 --database stu_220 > stu.sql 
将数据库stu_220中的所有数据备份到 stu.sql中


## 数据存储形式
1. 结构化  半结构化   非结构化数据

学习docker
预习函数式编程