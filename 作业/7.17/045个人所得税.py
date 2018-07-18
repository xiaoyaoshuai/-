money = int(input('请输入您的收入:'))
if money <= 3500:
    print('您不需要交税')
elif money >3500:
    a = money -3500
    if a<=1500:
        print(a*0.03,money-a*0.03)
    elif a<=4500:
        print(a*0.1,money-a*0.1)
    elif a<=9000:
        print(a*0.2,money-a*0.2)
    elif a<=35000:
        print(a*0.25,money-a*0.25)
    elif a<=55000:
        print(a*0.3,money-a*0.3)
    elif a<=80000:
        print(a*0.35,money-a*0.35)
    elif a>80000:
        print(a*0.45,money-a*-.45)
