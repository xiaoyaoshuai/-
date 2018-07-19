def fun_checkout():
    print('开始计算--->')
    print('')
    l = []
    while True:
        money = float(input('请输入金额(输入0表示输入完毕)：'))
        l.append(money)
        if money == 0:
            break
    allmoney = 0        
    a = 0
    for i in l:
        allmoney += i
    if allmoney >= 500 and allmoney < 1000:
        a = allmoney * 0.9
    elif allmoney >= 1000 and allmoney < 2000:
        a = allmoney * 0.8
    elif allmoney >= 2000 and allmoney < 3000:
        a = allmoney * 0.7
    elif allmoney >= 3000:
        a = allmoney * 0.6
    print('合计金额%.2f,实付金额%.2f'%(allmoney,a))    
fun_checkout()    
