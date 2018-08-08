class Dl():
    def __new__():
        return super().__init__()
    def __init__(self,name):
        self.name = name
        print('他的名字%s'%self.name)
a = Dl('张三')
print(a.name)

