'''
请使用for循环计算1~100之间偶数的和
'''
sum = 0
for a in range (1,101):
    if a % 2 == 0:
        sum = sum + a
print('1~100偶数的值:%d'%sum)        
