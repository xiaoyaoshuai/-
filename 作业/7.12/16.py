name = str(input ('请您输入姓名'))
print ('%s您好,对应的星座:(1)水瓶,1月20~2月18;(2)双鱼,2月19~3月20;(3)双鱼,3月31~4月19;(4)金牛,4月20~5月20;(5)双子,5月21~6月21;(6)巨蟹,6月21~7月22;(7)狮子,7月21~7月22;(8)处女,8月23~9月22' %name)
count = int(input('请输入对应编号'))
if count == 1:
    print('%s,您好!您的星座分析:日期是1月20~2月18，性格腼腆' %name)
elif count == 2:
    print('%s,您好!您的星座分析:日期是2月19~3月20，性格冲动' %name)
elif count == 3:    
    print('%s,您好!您的星座分析:日期是3月21~4月19，性格温顺' %name)
elif count == 4:    
    print('%s,您好!您的星座分析:日期是4月20~5月20，性格暴躁' %name)
elif count == 5:    
    print('%s,您好!您的星座分析:日期是5月21~6月21，性格和谐' %name)
elif count == 6:    
    print('%s,您好!您的星座分析:日期是6月22~7月22，性格张狂' %name)
elif count == 7:    
    print('%s,您好!您的星座分析:日期是7月24~8月22，性格骄傲' %name)
elif count == 8:    
    print('%s,您好!您的星座分析:日期是8月23~8月22，性格讲究' %name)
