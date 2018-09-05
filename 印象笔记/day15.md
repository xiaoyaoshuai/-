---
title: day 15
tags: 
notebook: 数据库
---
1. 大话数据结构   大话数据模式



# 数据库
## 索引
1. 索引的存储类型
B-TREE 索引   HASH索引  R-Tree(空间)索引   FULL-text(全文)索引 
B-TREE索引
2. show index from students;
show index from students  查看支持的索引
3. create index name_index on students_more(name); 创建索引
4. sudo apt install mysli
5. show index from students_more;
6. drop index name_index on students_more;
7. 删除索引
DROP INDEX index_name ON talbe_name
ALTER TABLE table_name DROP INDEX index_name
ALTER TABLE table_name DROP PRIMARY KEY

## 安全管理
1. RBAC(Role-Based Access Control)基于角色的权限访问控制
设置访问 grant select on stu_220.* to hd;
show grants for hd;
2. 查看有哪些用户
use mysql;   select user from user;
3. 创建用户
create user hd identified by “abcd1234”; 
4. 重命名用户
rename user hd to dh ;
5. 删除用户
drop user dh  ;
6. 设置访问权限
为看到赋予用户账号的权限,使用 SHOW GRANTS FOR hd
7. grant select on stu_1803.* to hd;
show grants for hd;
8. grant的反操作为revoke，用来撤销特定的权限，revoke select on stu_1803.* from hd;
9. grant和revoke可在几个层次上控制访问权限：
整个服务器，使用grant all和revoke all
整个数据库，使用on database.*
特定的表，使用on database.table
特定的列
10. SELECT
SHOW DATABASES 使用SHOW DATABASES
SHOW VIEW 使用SHOW CREATE VIEW
SHUTDOWN 使用mysqladmin shutdown(用来关闭MySQL)
使用CHANGE MASTER、KILL、LOGS、PURGE、MASTER
和SET GLOBAL。还允许mysqladmin调试登录
SUPER
UPDATE 使用UPDATE
USAGE 无访问权限
11. SET PASSWORD 还可以用来设置你自己的口令
set password for hd = “abcd1234”
12. grant all . to root@'%' IDENTIFIED by 'abcd1234';



