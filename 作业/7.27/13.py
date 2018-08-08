python = set(['绮梦','冷伊一','香凝','梓轩']) # 保存选择python语言的学生姓名
c = set(['冷伊一','零语','梓轩','圣博']) # 保存选择C语言的学生姓名
print('选择python语言的学生有:',python) # 输出选择python语言的学生
print('选择C语言的学生有:',c) # 输出选择c语言的学生
print('交集运算:',python&c) # 选择python语言又选择了C语言
print('并集运算:',python|c) # 输出全部参与选课的学生的名字
print('差集运算',c-python) # 输出只选择python语言但是没有选择c语言的学生

