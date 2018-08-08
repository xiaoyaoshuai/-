import random
i = 0
n = random.randint(1,100)
while True:
    u = int(input('请输入1-100的整数'))
    i += 1
    if u > n:
        print('数字大了')
    elif u < n: 
        print('数字小了')
    else:
        print('猜对了')
        break
print('一共猜了{}次'.format(i))

