---
title: day 4
tags: 
notebook: 数据库
---
# linux
1. /dev/null  
/dev/null : 在类Unix系统中，/dev/null，或称空设备，是一个特殊的设备文件，它丢弃一切写入其中的数据（但报告写入操作成功），读取它则会立即得到一个EOF。
/dev/null 日常使用

(1). 把/dev/null看作"黑洞"。它等价于一个只写文件，并且所有写入它的内容都会永远丢失，而尝试从它那儿读取内容则什么也读不到。然而, /dev/null对命令行和脚本都非常的有用。
(2). 另外还可以使用/dev/null，来清除文件中的内容，而不删除文件。
>vim 1.txt 写入 helloworld
cat 1.txt 查看内容
cat  /dev/null >1.txt
然后再次查看的时候就没有内容了

/dev/zreo 
>/dev/zero是类Unix操作系统中的一个特殊文件，用来提供一个空字符文件，其一个典型的应用就是提供字符流进行数据存储初始化。
/dev/zero的读操作会依据其请求返回大量的空字符。
不像 /dev/null, /dev/zero可能被用作资源，而不仅仅是用来做数据回收池。所有针对/dev/zero的写操作均OK，没有什么影响，不过，无用输出重定向还是/dev/null更适合。

kmp
# SQL
1. show table status \G  显示所有表信息
2. show engines; 查看系统中支持的引擎状态
3. show variables like 'default_storage_engine' 显示默认引擎   show variables like 'default%';
4. default_storage_engine = InnoDB 修改处理器
5. cd /etc/mysql/mysql.conf.d/mysqld.cnf 数据库配置文件
6. 引擎 处理事务  
>种类：InnoDB , MEMORY , BLACKHOLE ， MyIASM
7. select avg(age) from students; 查询students平均年龄
8. 字符串，数值型，日期时间，二进制
9. 创建语句
```SQL
    create table menu(
    mid tinyint prinmary key comment '主键，菜编号',
    name varchar(20) not null comment '菜名',
    price tinyint not null comment '价格',
    style varchar(100) not null comment '风格',
    size char(3) not null comment '规格'
)comment '刀削面菜谱'
```
10. alter table menu add phone int not null; 添加phone字段
11. alter table menu drop column phone ; 删除phone字段
12. alter table menu modify phone int(8) null default 18900000000;
13. delete from menu ; 清空表 一条一条删，速度慢
    alter table menus drop column address; 删除表中的address字节
14. truncate menu; 清空表 直接删除表，速度块
15. alter table menu add birthday date not null comment '生日' ;添加生日列
16.
```SQL
 create table student(id int auto_increment comment '学号',name varchar(50) not null comment '姓名',sex char(2) not null comment '性别',age int not null comment '年龄',birthday date not null comment '出生日期',id_card char(3) not null comment '证件类型',id_number char(18) not null comment '身份证号',phone char(11) not null comment '手机号',email varchar(50) not null comment '邮箱',place varchar(50) not null comment '籍贯',address varchar(50) not null comment '家庭住址',come_school date not null comment '入学时间',interest varchar(30) not null comment '兴趣爱好',first_name varchar(10) not null comment '首字母大写' ,primary key(id))comment '学生信息';
```
17. show create database stu 查看stu建立的详情
18. update students set age = 21 where id = 1504747; 修改编号1504747的年龄为21

