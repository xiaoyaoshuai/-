#设计一个Circle类,包括圆心的位置、半径、颜色等属性.编写构造方法和其他方法计算周长和面积.
class Circle():
    def __init__(self,name,radius):
        self.radius = radius
        self.name = name
    def color(self):
        print('%s圆是蓝色'%self.name)
    def zc(self):
        print('%s圆的周长:'%self.name,2*self.radius*3.14)
    def mj(self):
        print('{}圆的面积是:'.format(self.name),3.14*self.radius**2)
    def center(self):
        print('{}圆心在正中间'.format(self.name))
l = Circle('x',3)
l.zc()
l.mj()
l.color()
l.center()
