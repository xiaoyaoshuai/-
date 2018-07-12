import random
computer = random.randint(1,10)
player =int (input ("请玩家输入数字"))
print (computer)
if player == computer:
    print ('胜利')
else:
    print ('失败,你是一个loser')
