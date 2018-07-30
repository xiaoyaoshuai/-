print("在古希腊神话中，玫瑰集爱情与美丽与一身，所以人们常用玫瑰来表达爱情，但是不同的朵数的玫瑰花代表的含义是不同的")
flowers =int(input('请输入您想送几多玫瑰花,我会告诉你玫瑰花的含义：'))
if flowers == 1:
    print ('你是我的唯一')
elif flowers == 3:
    print ('I Love You')
elif flowers == 10:
    print ('十全十美')
elif flowers == 99:
    print ('天长地久')
elif flowers == 108:
    print ('求婚')
elif flowers == 999:
    print ('土豪')
else:
    print ('我也不知道它的含义,您可以考虑1,3,10,99,108,999')
     
