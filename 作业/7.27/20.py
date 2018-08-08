class Student(object):
    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores = scores
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.scores)
zs =Student ('张三',20,[89,79,98])
print(zs.get_name())
print(zs.get_age())
print(zs.get_course())
