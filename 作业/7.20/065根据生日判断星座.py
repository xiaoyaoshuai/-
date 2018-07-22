month = int(input('请输入月份(例如:5)'))
date = int(input('请输入日期(例如:17)'))
xz = None
if (month == 3 and date in range(21,32)) or (month == 4 and date in range(1,20)):
    xz = '白羊座'
elif (month == 4 and date in range(20,31)) or (month == 5 and date in range(1,21)):
    xz = '金牛座'
elif (month == 5 and date in range(21,32)) or (month == 6 and date in range(1,22)):
    xz = '双子座'
elif (month == 6 and date in range(22,31)) or (month == 7 and date in range(1,23)):
    xz = '巨蟹座'
elif (month == 7 and date in range(23,32)) or (month == 8 and date in range(1,23)):
    xz = '狮子座'
elif (month == 8 and date in range(23,32)) or (month == 9 and date in range(1,23)):
    xz = '处女座'
elif (month == 9 and date in range(23,31)) or (month == 10 and date in range(1,24)):
    xz = '天秤座'
elif (month == 10 and date in range(24,32)) or (month == 11 and date in range(1,23)):
    xz = '天蝎座'
elif (month == 11 and date in range(23,31)) or (month == 12 and date in range(1,22)):
    xz = '射手座'
elif (month == 12 and date in range(22,32)) or (month == 1 and date in range(1,20)):
    xz = '摩羯座'
elif (month == 1 and date in range(20,32)) or (month == 2 and date in range(1,19)):
    xz = '水瓶座'
elif (month == 2 and date in range(19,30)) or (month == 3 and date in range(1,21)):
    xz = '双鱼座'
print('%d月%d日星座为%s'%(month,date,xz))
