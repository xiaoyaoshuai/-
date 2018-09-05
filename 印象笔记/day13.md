---
title: day 13
tags: 
notebook: 数据库
---
1. yaml
2. select p1.name,p2.score
   from students as p1 join scores as p2
   on p1.stu_id = 1504769 and p2.id = 16;
# 视图
3. create view  students_score  as select p1.name,p2.score,p1.stu_id,p1.phone,p2.course 
   from students as p1 join scores as 
   p2 on p1.stu_id = p2.stu_id;
4. drop view  view_name;
5. isinstance(resule[5],datetime.date)


