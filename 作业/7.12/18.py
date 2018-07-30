number = '123456'
passwd = '123'
money = 10000
number1 = input ('请输入账号')
passwd1 = input ('请输入密码')
if (number1 == number and passwd1 == passwd):
    print ('输入正确,请选择取款金额')
    money1 = int(input ('请输入取款金额'))
    if money1 > money:
        print ('余额不足')
    elif money1 <= money:
        print ('此次取款%d元,剩余%d元'%(money1,money-money1))
    else:
        print ('余额不足')
else:
    print('非法账户')
