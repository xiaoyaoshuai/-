'''
实战三十: 求50~100之间的偶数之和并且输出
'''
count = 50 # count计数器
sum = 0
while count >= 50 and count <=100:
    if count % 2 == 0:
        sum += count
    count += 1
print (sum)
