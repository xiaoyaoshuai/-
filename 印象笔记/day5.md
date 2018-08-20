---
title: day5
tags: 
notebook: 数据库
---
# Python
1. uuid 
UUID 是 通用唯一识别码（Universally Unique Identifier）的缩写，是一种软件建构的标准，亦为开放软件基金会组织在分布式计算环境领域的一部分。其目的，是让分布式系统中的所有元素，都能有唯一的辨识信息，而不需要通过中央控制端来做辨识信息的指定。如此一来，每个人都可以创建不与其它人冲突的UUID。在这样的情况下，就不需考虑数据库创建时的名称重复问题。目前最广泛应用的UUID，是微软公司的全局唯一标识符（GUID），而其他重要的应用，则有Linux ext2/ext3文件系统、LUKS加密分区、GNOME、KDE、Mac OS X等等。另外我们也可以在e2fsprogs包中的UUID库找到实现。
UUID由以下几部分的组合：
（1）当前日期和时间，UUID的第一个部分与时间有关，如果你在生成一个UUID之后，过几秒又生成一个UUID，则第一个部分不同，其余相同。
（2）时钟序列。
（3）全局唯一的IEEE机器识别号，如果有网卡，从网卡MAC地址获得，没有网卡以其他方式获得。
```
import uuid
 
name = 'test_name'
namespace = 'test_namespace'
 
print uuid.uuid1()
print uuid.uuid3(namespace,name)
print uuid.uuid4()
print uuid.uuid5(namespace,name)
```
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
统计次数
select count(*) from badboy;
7. 表重命名
rename students to student