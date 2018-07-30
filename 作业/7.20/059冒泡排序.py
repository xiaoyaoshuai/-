a = input('')
l = list(a)
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j] > l[i]:
            l[j], l[i] = l[i], l[j]
print (l)


y = [1,9,4,7,3]
for x in range(len(y)):
    for z in range(len(y)-x-1):
        if y[z] > y[z+1]:
            y[z],y[z+1] = y[z+1],y[z]
print(y)
