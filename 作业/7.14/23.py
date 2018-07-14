count = 0
while count < 100:
    count = int(input ('请输入您的数字'))
    if count ==0:
        print ('')
    elif count > 0 and count < 100:
        print ('命运给予我们的不是失望之酒,而是机会之杯\n' * count)
print('退出')
