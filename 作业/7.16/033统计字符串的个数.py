'''
接收用户输入的一行字符,统计出字符串中包含数字的个数
'''
a =input('请您输入随机字符')
b = 0
for i in a:
    if i.isdecimal():
        b += 1
print (b)

