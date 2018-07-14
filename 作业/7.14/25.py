'''
实战二十五:求1~100之间能被7整除，但是同时不能被5整除的所有整数
'''
count = 1
while count <= 100:
    if count % 7 == 0 and count % 5 == 0:
        print (count)
    count += 1
