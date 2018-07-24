class Gun():
    def __init__(self,model):
        self.model = model
        self.bullet = 0
    def add_bullet(self,count):
        self.bullet += count
    def shoot(self):
        if self.bullet <= 0:
            print('没有子弹')
        else:
            self.bullet -= 1
            print('子弹发射了,还剩余[{}]'.format(self.bullet))
class Soldier():
    def __init__(self,name):
        self.name = name
        self.gun = None
    def fire(self):
        if self.gun is None:
            print('{}还没有枪'.format(self.name))
            return
        else:
            if self.gun.bullet <= 0:
                print('没有子弹')
            else:
                print('冲啊，打死他们')
                self.gun.shoot()
ak47 =Gun('ak47')                
xusanduo = Soldier('许三多')
xusanduo.gun = ak47
ak47.bullet = 50
xusanduo.fire()
