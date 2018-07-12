print('请输入您认为符合条件的数字')
i = int (input('请输入数字'))
if i % 3 ==2 and i % 5 ==3 and i % 7 ==2:
    print("符合条件")
else:
    print("不符合条件")
