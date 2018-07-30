'''
设计一个动物(Animal)类,该类包含颜色(color)属性和叫(call)方法.在设计一个表示鱼(Fish)的类,包括尾巴(tail)和颜色(color)两个属性,以及叫(call)方法. 提示:让Fish类继承自Animal类,重写__init__()和call方法
'''
class Animal():
    def __init__(self,color,call):
        self.color = color
        self.call = call
        print('{}{}'.format(self.color,self.call))
class Fish(Animal):
    def __init__(self,color,call):
        super().__init__(color,call)
        print('{}的鱼{}不会叫'.format(self.color,self.call))
    def tail(self):
        print('鱼有尾巴不会叫')
xiaochouyu = Fish('黄色','jj')
xiaochouyu.tail()
