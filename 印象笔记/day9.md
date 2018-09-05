---
title: day 9
tags: 
notebook: 数据库
---
# 正则表达式
1. 在线调试工具 http://tool.oschina.net/regex/  正则表达式匹配网站
2. 精通正则表达式 第三版 猫头鹰

# 数据库
1. select name from students where name regexp  '张';
2. select name,email from students where email    regexp  '.*@[^qq.com|out.outlook.com]';
2. select name,email from students where email    regexp  '.*@[^qq.com|out.outlook.com]';
3. select * from students where abbr_name regexp BINARY "G";
4. select name,email from students where email regexp ".*@[^outlook.com |^qq.com]";
5. select name,email from students where email regexp "^[0-9]";
6. select name,email from students where email regexp ".\..@";
7. select concat (name,'(',age,')') from students 