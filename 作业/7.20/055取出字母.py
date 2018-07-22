s = input ('请随机输入')
a = {}
s = s.lower()
for i in s:
    if i in a.keys():
        a[i] += 1
    else:
        a[i] = 1
print(a)
