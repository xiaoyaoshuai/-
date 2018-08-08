for i in range(100,1000):
    a = i // 100
    b = (i //10) % 10
    c = i % 10
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
print('-'*50)
s = 100
while s <= 999:
    a1 = s // 100
    b1 = (s //10) % 10
    c1 = s % 10
    if a1 ** 3 + b1 ** 3 + c1 ** 3 == s:
        print(s)
    s += 1
    
