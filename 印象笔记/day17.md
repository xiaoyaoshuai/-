---
title: day17
tags: hd
notebook: 数据库
---
# 获得人生中的成功需要的专注与坚持不懈多过天才与机会
# python
1. 反射 setattr getattr hasattr delattr
2. lt: less than 小于
   le: less than or equal to 小于等于
   eq: equal ro 等于
   ne: not equal to 不等于
   ge:greater than or equal to 大于等于
   gt: greater than 大于
## 迭代器-
3. 判断是否可迭代对象  __iter()__   __getitem()__
a = []
hasattr(a,'__iter__')
from collections import Iterable
isinstance((),Iterable)
4. 元组,列表,字典和字符串对象是可迭代的,但并不是迭代器,用iter()函数获得一个迭代器对象
python的for循环实质上是先通过内置函数iter()获得一个迭代器,然后不断调用next()函数实现的
```python
my_str = 'abc'
my_iter = iter(my_str)
next(my_iter)
```
## 生成器
```python
b =(i for i in range(999999999999))
next(b)
```
scrapy  教程
yield

