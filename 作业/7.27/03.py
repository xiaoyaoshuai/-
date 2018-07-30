def h():
    height = int(input('请输入身高(厘米)'))
    weight = int(input('请输入体重'))
    b = height - 100
    w = weight - b
    bl = float(w) / float(weight)
    while height < 250 and height > 30:
        if bl >= -0.05 and bl <= 0.05:
            print('体重正常')
            return
        else:
            print('体重超标或体重不达标')
            return
    ex= Exception('出现异常，身高错误')
    raise ex
try:
    h()
except Exception as ex:
    print(ex)
