import random
while True:
    computer = random.randint(1,3)
    player = int(input('请输入1拳头2布3剪刀'))
    if (computer == 1 and player) == 2 or (computer == 2 and player == 3) or (computer == 3 and player == 1):
        print('你赢了')
        break
    elif computer == player:
        print('平局')
    else:
        print('电脑赢了')
