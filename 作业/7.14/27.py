'''
实战二十七:求200以内能被17整除的最大整数
'''
count = 0
a = 0
while count <= 200:
    if count % 17 ==0:
        a=count
    count += 1
print(a)
