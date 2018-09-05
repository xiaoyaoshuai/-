---
title: day7 
tags: 
notebook: 数据库
---
# 数据库

## 1.通配符 '%'
匹配一个或多个字符
1. select name,place from students where name like '李%' ;
2. select name,place from students where name like '%泳%' ; 
%不区分大小写
2. select name from students where trim(name) like '%三';  三后面有空格时用trim
3. select name from students where email is null ;

## 2.通配符  '_'
匹配一个字符
1. select name from students where name like '刘_' ;
2. select name from students where name like '_泳_' ;

## 3.字段
1. select concat(name,'(',place,')') from students; 将两个列合并
2. select concat(name,'(',place,')') as new_name from students;将合并的列命名为new_name;
3. select name,count*price as total from menus ;算出总价
安装库连接
pip3 install mysql-connector
sudo apt-get install libmysqlclient-dev 
pip3 install mysql-connector

# linux
1. alias 

alias命令用来设置指令的别名。我们可以使用该命令可以将一些较长的命令进行简化。使用alias时，用户必须使用单引号''将原来的命令引起来，防止特殊字符导致错误。

alias命令的作用只局限于该次登入的操作。若要每次登入都能够使用这些命令别名，则可将相应的alias命令存放到bash的初始化文件/etc/bashrc中。

alias 新的命令='原命令 -选项/参数'
例如：alias l=‘ls -lsh'将重新定义ls命令，现在只需输入l就可以列目录了。直接输入 alias 命令会列出当前系统中所有已经定义的命令别名。

要删除一个别名，可以使用 unalias 命令，如 unalias l。
2. ~ 家目录 
3. ~ .bashrc   .profile
>要搞清bashrc与profile的区别，首先要弄明白什么是交互式shell和非交互式shell，什么是login shell 和non-login shell。
交互式模式就是shell等待你的输入，并且执行你提交的命令。这种模式被称作交互式是因为shell与用户进行交互。这种模式也是大多数用户非常熟悉的：登录、执行一些命令、签退。当你签退后，shell也终止了。 shell也可以运行在另外一种模式：非交互式模式。在这种模式下，shell不与你进行交互，而是读取存放在文件中的命令,并且执行它们。当它读到文件的结尾，shell也就终止了。
bashrc与profile都用于保存用户的环境信息，bashrc用于交互式non-loginshell，而profile用于交互式login shell。系统中存在许多bashrc和profile文件，下面逐一介绍：
/etc/pro此文件为系统的每个用户设置环境信息,当第一个用户登录时,该文件被执行.
并从/etc/profile.d目录的配置文件中搜集shell的设置.
/etc/bashrc:为每一个运行bash shell的用户执行此文件.当bash shell被打开时,该文件被读取。有些linux版本中的/etc目录下已经没有了bashrc文件。
~/. pro每个用户都可使用该文件输入专用于自己使用的shell信息,当用户登录时,该
文件仅仅执行一次!默认情况下,它设置一些环境变量,然后执行用户的.bashrc文件.
~/.bashrc:该文件包含专用于某个用户的bash shell的bash信息,当该用户登录时以及每次打开新的shell时,该文件被读取.
另外,/etc/profile中设定的变量(全局)的可以作用于任何用户,而~/.bashrc等中设定的变量(局部)只能继承/etc/profile中的变量,他们是"父子"关系
4. vim /etc/profile
vim bash.bashrc
/etc/profile，/etc/bashrc 是系统全局环境变量设定
~/.profile，~/.bashrc用户家目录下的私有环境变量设定
当登入系统时候获得一个shell进程时，其读取环境设定档有三步
1首先读入的是全局环境变量设定档/etc/profile，然后根据其内容读取额外的设定的文档，如
/etc/profile.d和/etc/inputrc
2然后根据不同使用者帐号，去其家目录读取~/.bash_profile，如果这读取不了就读取~/.bash_login，这个也读取不了才会读取
~/.profile，这三个文档设定基本上是一样的，读取有优先关系
3然后在根据用户帐号读取~/.bashrc
至于~/.profile与~/.bashrc的不区别
都具有个性化定制功能
~/.profile可以设定本用户专有的路径，环境变量，等，它只能登入的时候执行一次
~/.bashrc也是某用户专有设定文档，可以设定路径，命令别名，每次shell script的执行都会使用它一次
5. ctrl + r 出现命令搜索框

# python
1. utc
整个地球分为二十四时区，每个时区都有自己的本地时间。在国际无线电通信场合，为了统一起见，使用一个统一的时间，称为通用协调时(UTC, Universal Time Coordinated)。UTC与格林尼治平均时(GMT, Greenwich Mean Time)一样，都与英国伦敦的本地时相同。在本文中，UTC与GMT含义完全相同。
2. iso8601 时间格式
3. unix timestamp time.time()
时间戳是自 1970 年 1 月 1 日（00:00:00 GMT）以来的秒数。它也被称为 Unix 时间戳(Unix Timestamp）。
4. json 
JSON(JavaScript Object Notation, JS 对象简谱) 是一种轻量级的数据交换格式。它基于 ECMAScript (欧洲计算机协会制定的js规范)的一个子集，采用完全独立于编程语言的文本格式来存储和表示数据。简洁和清晰的层次结构使得 JSON 成为理想的数据交换语言。 易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率
dumps   loads
dumps是将dict转化成str格式，loads是将str转化成dict格式。

| josn | python |
| --- | --- |
object | dict
array | list
string|str
number(int)|int
number(real)|float
true|True
false|False
null|None

5. time.time
now_str = datetime.date.strftime(now,'%Y-%m-%d %H:%M:%S %f')
datetime.datetime.strptime("2018-08-16 08:13:27","%Y-%m-%d %H:%M:%S")
6. for _ in range(100) _占位符,只执行循环内的语句