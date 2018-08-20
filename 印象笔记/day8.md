---
title: day8
tags: 
notebook: 数据库
---
# python
1. 日期对象
datetime.datetime.now()
time.time()
time.localtime()
datetime.datetime.now().date()
datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
datetime.date.today() + datetime.timedelta(days=30)
datetime.datetime.combine(datetime.date.today(),datetime.time())
datetime.datetime.combine(datetime.date.today(),datetime.time.min)
datetime.datetime.combine(datetime.date.today(),datetime.time.max)
timestmap = time.mktime(now.timetuple())
datetime.datetime.fromtimestamp(1534467288.0)
pip3 install XlsxWriter
```
import mysql.connector as c
db = c.connect(user='root',passwd = 'abcd1234',database = 'stu_220',host='192.168.4.14')
cursor = db.cursor()
sql = 'select name,phone,place from students'
cursor.execute(sql)
result = cursor.fetchall()
import xlsxwriter,datetime
workbook = xlsxwriter.Workbook('学生信息.xlsx')
worksheet = workbook.add_worksheet()
for index,values in enumerate(result):
    worksheet.write('A{}'.format(index),values[0])
    worksheet.write('B{}'.format(index),values[1])
    worksheet.write('C{}'.format(index),values[2])
```

