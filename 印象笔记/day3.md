---
title: day3
tags: 
notebook: 数据库
---
# python
1. chr 
>返回以数值表达式值为编码的字符,其数值表达式值取值范围为0~255
2. unicode
    >Unicode（统一码、万国码、单一码）是计算机科学领域里的一项业界标准,包括字符集、编码方案等。Unicode 是为了解决传统的字符编码方案的局限而产生的，它为每种语言中的每个字符设定了统一并且唯一的二进制编码，以满足跨语言、跨平台进行文本转换、处理的要求
utf-8
    >UTF-8（8-bit Unicode Transformation Format）是一种针对Unicode的可变长度字符编码，又称万国码，由Ken Thompson于1992年创建。现在已经标准化为RFC 3629。UTF-8用1到6个字节编码Unicode字符。用在网页上可以统一页面显示中文简体繁体及其它语言（如英文，日文，韩文）
# linux 
1. ps aux 查看进程
2. tcp/ip 传输控制协议/因特网互联协议，又名网络通讯协议
3. sla 了解
>LA：Service-Level Agreement的缩写，意思是服务等级协议。
是关于网络服务供应商和客户间的一份合同，其中定义了服务类型、服务质量和客户付款等术语。
4. /etc/hosts 
>hosts文件是Linux系统上一个负责ip地址与域名快速解析的文件，以ascii格式保存在/etc/目录下。hosts文件包含了ip地址与主机名之间的映射，还包括主机的别名。
5. fqdn
>FQDN：(Fully Qualified Domain Name)全限定域名：同时带有主机名和域名的名称。（通过符号“.”）
   dns
>(Domain Name System，域名系统），万维网上作为域名和IP地址相互映射的一个分布式数据库，能够使用户更方便的访问互联网，而不用去记住能够被机器直接读取的IP数串。通过域名，最终得到该域名对应的IP地址的过程叫做域名解析（或主机名解析）。DNS协议运行在UDP协议之上，使用端口号53。
# 数据库
1. 联机工具
2. cs架构
>Client/Server架构，即客户端/服务器架构。是大家熟知的软件系统体系结构，通过将任务合理分配到Client端和Server端，降低了系统的通讯开销，需要安装客户端才可进行管理操作。B/S架构：客户端基本上没有专门的应用程序，应用程序基本上都在服务器端
3. mysql - hPup  h地址 hosts P 端口 u 账户 p 密码
4. 登录流程
5. use databases;
6. help
7. show databases; 显示当前所有数据库名称
8. show tables; 显示当前数据库中所有表的名称
9. >错误代码
         130 ：文件格式不正确。（还不是很清楚错误的状况）

         145  ：文件无法打开。

         1005：MYSQL创建表失败
　　
　　1006：MYSQL创建数据库失败
　　
　     1007：MYSQL数据库已存在，创建数据库失败
　　
　　1008：MYSQL数据库不存在，删除数据库失败
　　
　　1009：MYSQL不能删除数据库文件导致删除数据库失败
　　
　　1010：MYSQL不能删除数据目录导致删除数据库失败
　　
         1011：MYSQL删除数据库文件失败
　　
　　1012：MYSQL不能读取系统表中的记录

　　1016：文件无法打开，使用后台修复或者使用 phpmyadmin 进行修复。
                     Quote:
                      开始=>所有程序=>附件=>命令提示符
                      输入 mysql 所在硬盘盘符
                      cd mysql 所在目录
                      cd bin
                      输入 myisamchk -f D:usr/local/mysql/data/bbs/PW_members.MYI
                      ps : D:usr/local/mysql/data/bbs 是你论坛数据库的路径
                      -f 根据具体情况选择，一般也可以选择 -r
                      注意你的 系统C盘或放数据库的硬盘空间是否足够，一般小于 1G 很容易出现错误。
                      或用mysqlcheck命令进行修复。具体的方法：利用命令行进入mysql/bin目录，执行
                      mysqlcheck -o -r phpwind -uroot -p                                                      
                      其中phpwind是你数据库的名称，root是你的数据库用户名，然后会提示你输入密码。然后就会修
                      复你的数据库。

         1017：服务器非法关机，导致该文件损坏。

　　1020：MYSQL记录已被其他用户修改
　　
　　1021：硬盘剩余空间不足，请加大硬盘可用空间
　　
　　1022：MYSQL关键字重复，更改记录失败
　　
　　1023：MYSQL关闭时发生错误
　　
　　1024：MYSQL读文件错误
　　
　　1025：MYSQL更改名字时发生错误
　　
　　1026：MYSQL写文件错误
　　
　　1030：可能是服务器不稳定。（具体原因不是很清楚）

         1032：MYSQL记录不存在
　　
　　1036：MYSQL数据表是只读的，不能对它进行修改
　　
　　1037：系统内存不足，请重启数据库或重启服务器
　　
　　1038：MYSQL用于排序的内存不足，请增大排序缓冲区
　　
　　1040：MYSQL已到达数据库的最大连接数，请加大数据库可用连接数
                      Quote:
                      在my.ini 修改max_connections=100为max_connections=1000或更大,重启mysql
　
　　1041：系统内存不足
　　
　　1042：无效的主机名
　　
　　1043：无效连接
　　
　　1044：MYSQL当前用户没有访问数据库的权限
　　
　　1045：MYSQL不能连接数据库，服务器、数据库名、用户名或密码错误
　              　Quote:
                      方法:确保论坛data目录下的sql_config.php用户名与密码都正确.如果用户忘记了数据库的密码,
                      可以按如下方式进行密码的修改:
                      如果 MySQL 正在运行，首先停止。
                      启动 MySQL ：bin/safe_mysqld --skip-grant-tables & 
                      就可以不需要密码就进入 MySQL 了。
                      然后就是
                      >use mysql
                      >update user set password=password("new_pass") where user="root";
                      >flush privileges;

          1046：没有选择数据库。

　　1048：MYSQL字段不能为空
　　
　　1049：MYSQL数据库不存在
　　
　　1050：MYSQL数据表已存在
　　
　　1051：MYSQL数据表不存在
　　
　　1054：MYSQL字段不存在，自行建立字段

　　1060：字段重复，导致无法插入这个字段。

         1062：字段值重复，入库失败
                      Quote:
                      1.如果出类似主码为"65535"的错误,可以查看相关表的自增字段,将字段值改在就可以
                      2.确保相关数据表中主码重复的字段是否存在,如果存在删除这条记录
                      3.备份数据库,修复相关表(注:这种情况比较常见,如pw_posts表,对表进行修复的时候不要忘记备份).

          1064：MySQL 不支持错误提示中的编码。

　　1065：MYSQL无效的SQL语句，SQL语句为空

　　1067：MySQL 版本为 5，不支持空的默认值。

　　1081：MYSQL不能建立Socket连接
　　
　　1114：MYSQL数据表已满，不能容纳任何记录
　　
　　1116：MYSQL打开的数据表太多
　　
　　1129：MYSQL数据库出现异常，请重启数据库
　　
　　1130：MYSQL连接数据库失败，没有连接数据库的权限
　　
　　1133：MYSQL数据库用户不存在

　　1135：可能是内存不足够，请联系空间商解决。

　　1141：MYSQL当前用户无权访问数据库
　　
　　1142：MYSQL当前用户无权访问数据表
　　
　　1143：MYSQL当前用户无权访问数据表中的字段
　　
　　1146：MYSQL数据表不存在或数据表缺失，请恢复备份数据
　　
　　1147：MYSQL未定义用户对数据表的访问权限
　　
　　1149：MYSQL语句语法错误
　　
　　1158：网络错误，出现读错误，请检查网络连接状况
　　
　　1159：网络错误，读超时，请检查网络连接状况
　　
　　1160：网络错误，出现写错误，请检查网络连接状况
　　
　　1161：网络错误，写超时，请检查网络连接状况
　　
　　1062：MYSQL字段值重复，入库失败
　　
　　1169：MYSQL字段值重复，更新记录失败
　　
　　1177：MYSQL打开数据表失败
　　
　　1180：MYSQL提交事务失败
　　
　　1181：MYSQL回滚事务失败
　　
　　1203：MYSQL当前用户和数据库建立的连接已到达数据库的最大连接数，请增大可用的数据库连接数或 
                       重启数据库
　　
　　1205：MYSQL加锁超时
　　
　　1211：MYSQL当前用户没有创建用户的权限
　　
　　1216：MYSQL外键约束检查失败，更新子表记录失败
　　
　　1217：MYSQL外键约束检查失败，删除或修改主表记录失败
　　
　　1226：MYSQL当前用户使用的资源已超过所允许的资源，请重启数据库或重启服务器
　　
　　1227：MYSQL权限不足，您无权进行此操作
　　
　　1235：MySQL版本过低，不具有本功能

          1250：客户端不支持服务器要求的认证协议，请考虑升级客户端。

          1251：Client 不能支持 authentication protocol 的要求
                      Client does not support authentication protocol requested by server; consider upgrading MySQL client
                      Quote:
                      方法1：
                                  mysql> SET PASSWORD FOR
                                         -> ' some_user '@' some_host ' = OLD_PASSWORD(' newpwd '); 
                      结合我们的实际情况,在 MySQL Command Line Client 下运行:
                      set password for root@localhost = old_password('123456');

                      方法2：
　　　　　　　mysql> UPDATE mysql.user SET Password = OLD_PASSWORD('newpwd')
    　　　　　　　　-> WHERE Host = 'some_host' AND User = 'some_user';
　　　　　　　mysql> FLUSH PRIVILEGES;
                           <上面的部分请按自己实际情况修改。>

        1267：不合法的混合字符集。

        2002：服务器端口不对，请咨询空间商正确的端口。

        2003：MySQL 服务没有启动，请启动该服务。

        2008：MySQL client ran out of memory
                    错误指向了MySQL客户mysql。这个错误的原因很简单，客户没有足够的内存存储全部结果。

        2013：远程连接数据库是有时会有这个问题，MySQL 服务器在执行一条 SQL 语句的时候
                    失去了连接造成的。

        10048：最大连接数等问题
　　　　  　 Quote:
                        建议在my.ini文件中修改最大连接数，
                        把 mysql_connect() 方法都改成了 mysql_pconnect() 方法.
                        要修改mysql_pconnect()，可以在论坛的data目录的sql_config.php中
                        $pconnect = 0; //是否持久连接
                        修改成$pconnect = 1;
                        开启防刷新,严禁刷新太快.

        10055：没有缓存空间可利用
                        Quote:
                        查看下你的C盘空间是否已经满,清除一些没有用的文件.
                        可以在后台的"论坛核心设置","核心功能设置"里"进程优化"开启,"GZIP 压缩输出"关闭.
                        查找了一下10055（没有缓存空间可利用）出错的原因，分析了my.ini的配制文件，
                        在my.ini中如下：
                        default-storage-engine=INNODB
                         innodb_additional_mem_pool_size=2M
                         innodb_flush_log_at_trx_commit=1
                         innodb_log_buffer_size=1M
                         innodb_buffer_pool_size=10M
                         innodb_log_file_size=10M
                         innodb_thread_concurrency=8
                         觉得可以把innodb_buffer_pool_size=10M　加大如100M或是1000M
                         以上是对mysql5的

                         如果是mysql4可以在my.ini中增加如下：
                         #innodb_data_file_path = ibdata1：2000M;ibdata2：2000M
                         #innodb_data_home_dir = c：ibdata
                         #innodb_log_group_home_dir = c：iblogs
                         #innodb_log_arch_dir = c：iblogs
                         #set-variable = innodb_mirrored_log_groups=1
                         #set-variable = innodb_log_files_in_group=3
                         #set-variable = innodb_log_file_size=5M
                         #set-variable = innodb_log_buffer_size=8M
                         #innodb_flush_log_at_trx_commit=1
                         #innodb_log_archive=0
                         #set-variable = innodb_buffer_pool_size=16M
                         #set-variable = innodb_additional_mem_pool_size=2M
                         #set-variable = innodb_file_io_threads=4
                         #set-variable = innodb_lock_wait_timeout=50
                         把前面的#去了

        10061：MySQL服务不能正常启动
                        Quote:
                        启动这台机器上的MySQL服务 
                        如服务启动失败，一定是你的my.ini文件出了差错， MySQL服务不能正常启动 
                        你删除了它后，MySQL就会按其默认配置运行，那就没有问题了
>数据库操作
10. show grants;查看用户的数据库权限
11. show status；可以检查mysql当前的状态
12. 库、表、列、行、数据类型，主键
13. drop database xxx 删除数据库
14. creat database stu_220 ; 创建stu_220数据库
15. show creat database stu_220 ; 展示创建的数据库
16. create database stu_220 charset = 'utf8';可以不用=号  创建stu_220的数据库
17. create database if not exists stu_220 ; 创建数据库如果存在
18. drop database if exists stu_220 ; 删除数据库如果存在
19. >创建表格
 ```   
    create table students(
                    id int auto_increment comment '学号',
                    name varchar(50) not null comment '姓名',
                    age int not null comment '年龄',
                    sex char(2) not null comment '性别'，
                    primary key(id)) comment '学生信息';                
```
20. insert into students values(1506666,'田真',23,'女') 往表里面插入表 
21. select * from students ; 查看表里面的内容
22. show create table students;
23. desc students ; 查看表结构
24. show table status \G 查看表状态

quora网站