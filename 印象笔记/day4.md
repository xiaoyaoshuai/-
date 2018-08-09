---
title: day 4
tags: 
notebook: 数据库
---
# linux
1. /dev/null    /dev/zreo   kmp
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
14. truncate menu; 清空表 直接删除表，速度块
15. alter table menu add birthday date not null comment '生日' ;添加生日列
16. 