print ("------跳一跳，输入‘退出’即可退出游戏------")
score = None
print ('欢迎回来，请开始游戏')
print ('请输入\(中心、音乐模块、微信支付模块)')
while score != '退出':
    score = input ('请输入:')
    if score == '中心':
        print ('您的分数为:32')
    elif score =='音乐模块':
        print ('您的分数为：30')
    elif score == '微信支付模块':
        print ('您的分数:42')
    elif score == '退出':
        pass
    else:
        print ('输入有误，请重新输入')
print ('已退出')

