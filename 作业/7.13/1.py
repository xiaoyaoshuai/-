row = 1
while row <= 9:
   a = 1
   while a <= row:
       print('%d*%d=%d' %(a,row,a*row),end='\t')
       a += 1       
   print('')
   row += 1
