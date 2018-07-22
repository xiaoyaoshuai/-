s = input('请输入个数为奇数位的数字若干')
for i,c in enumerate(s):
    num = 0
    num += i
a = num // 2
print(s[a])
