'''
设计一个课程类,包括课程编号、课程名称、任课老师、上课地点等属性,把上课地点的变量设为私有的,增加构造方法和显示课程信息的方法
'''
class Course():#课程类
    def __init__(self,number,name,teacher):
        self.number = number
        self.name = name
        self.teacher = teacher
        print('第{}节课{}课程是{}老师的课'.format(self.number,self.name,self.teacher))
    def __adress(self):
        print('220教室')
kc = Course('1','python基础','翁总')
print(kc._Course__adress())
