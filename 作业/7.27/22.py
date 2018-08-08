class Animal():
    def __init__(self,name):
        self.name = name
    def call(self):
        print('%s在叫'%self.name)
class Dog(Animal):
    def run(self):
        print('{}在跑'.format(self.name))
    def pname(self):
        print('名字{}'.format(self.name))
ws = Dog('小白')
ws.run()
ws.pname()
