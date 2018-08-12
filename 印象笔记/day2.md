---
title: day2
tags: 
notebook: 数据库
---
# Linux
1. netstat 用来打印Linux中网络系统的状态信息，可让你得知整个Linux系统的网络情况
        netstat -nat | grep 3306  查看端口3306的运行程序
    -a 显示所有连线中的Socket
    -n或--numeric：直接使用ip地址，而不通过域名服务器
    -t或--tcp：显示TCP传输协议的连线状况
2. lsof -i:3306 查询3306是谁在使用这个端口
        lsof -v 查看版本信息
        -i<条件>：列出符合条件的进程。（4、6、协议、:端口、 @ip ）
3. systemctl status mysql  或者 service mysql status 查看服务状态
   systemctl restart mysql 或者 service mysql restart 重启
   mysql  start  stop
4. man
5. 注释已有的配置添加新的配置
# Python
1. pickle持久化的储存数据
   ```     
        import pickle
        a = {" name ": "Tom", "age": "40"}
        with open(‘text.txt‘, ‘wb‘) as file:    
            pickle.dump(a, file) 
        with open(‘text.txt‘, ‘rb‘) as file2:    
            b = pickle.load(file2)
        print(type(b))
        print(b)
```
2. json
# 数据库
1. DB
    数据库简称
2. DBNS
    数据库管理系统
3. SQL
    是一种数据库查询和程序设计语言
4. MySQL
    是一种数据库类型
5. 其他的数据库管理系统 
    SQL Server、Oracle、Sybase、DB2
6. 集群 --->集群通信系统是一种用于集团调度指挥通信的移动通信系统，主要应用在专业移动通信领域。
负载均衡器--->其意思就是分摊到多个操作单元上进行执行
高可用集群--->高可用是指同一时间提供服务的只有一台设备，主服务器挂掉后，备用服务器便开始提供服务。
7. ubuntu包管理 apk dpkg
8. MySQL安装
    sudo apt update
    sudo apt install mysql-server
9. 配置
    配置文件路径
    bind-address 127.0.0.1  to 0.0.0.0
    port
10. MySQL联机工具第一次登录
    