'''
设计一个表示学生(Student)的类,该类属性有名字(name),年龄(age),成绩(scores)(成绩包含语文,数学和英语三科成绩,每科成绩的类型为整数)另外有3个方法. (1) 获取学生姓名的方法:get_name(),返回类型为String (2) 获取学生年龄的方法:get_age()方法,返回类型为Int (3) 返回3门科目中最高的分数,get_course(),返回类型为Int
'''
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('我叫{},今年{}岁'.format(self.name,self.age))
    def scores(self,chinese,math,english):
        self.chinese = chinese
        self.math = math
        self.english = english
        print('语文{:.0f},数学{:.0f},英语{:.0f}'.format(chinese,math,english))
    def max_scores(self):
        print ('最高成绩为',max(ws.chinese,ws.english,ws.math))
        return 
ws = Student('王帅',25)
ws.scores(91,98,109)
ws.max_scores()
