---
title: day18
tags: hd
notebook: 数据库 
---
create table user(
    id int auto_increment primary key not null comment '用户id',
    name varchar(10) not null comment '用户名',
    email varchar(50) not null comment '邮箱',
    sex char(2) not null comment '性别',
    vip char(2) not null comment '是否VIP')comment '用户信息表';
授权root用户
  grant all on *.* to root@“%” identified by “root用户密码” ;

  刷新权限
  flush privileges; 

  退出联机工具
  exit
