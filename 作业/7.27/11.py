import random
l = {random.randint(10,100) for i in range(10)}
print(l)


print('-'*50)

price = [10,24,54,13,63]
sale = [int(i*0.5) for i in price]
print(price)
print(sale)
print('*'*50)


s = [12,332,14,578,54]
c = [x for x in s if x>100]
print(c)
