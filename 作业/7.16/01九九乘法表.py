'''
请使用for循环写一个九九乘法表
'''
for a in range(1,10):
    for b in range(1,a+1):
        c = a * b
        print ('%d*%d=%d'%(b,a,c),end='\t')
    print ('')
