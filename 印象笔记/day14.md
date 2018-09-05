---
title: day 14
tags: 
notebook: 数据库
---
# 数据库



# python
1. locals()
2. globals()
3. posix

1. select id,stu_id,score from scores where score <31 union SELECT id,stu_id ,score from scores where stu_id in (1504760,1504858);

2. select id,stu_id,score from scores where score
<31 union SELECT id,stu_id ,score from scores where stu_id in (1504760,1504858) order by score desc ;

3. select id,stu_id,score from scores where score
<31 union all SELECT id,stu_id ,score from scores where stu_id in (1504760,1504858);