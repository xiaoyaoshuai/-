num = 0
for i in range(1,100):
    if i % 7 ==0  or i % 10 == 7:
        num += 1
    continue
print('从1到99共拍腿%d次。'%num)
