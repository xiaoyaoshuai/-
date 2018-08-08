i = 1
while i <= 9:
    l = 1
    while l <= i:
        print('{}*{}={}'.format(l,i,l*i),end='\t')
        l += 1
    i += 1
    print('')    
print('*'*60)
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(j,i,j*i),end = '\t')
    print('')
