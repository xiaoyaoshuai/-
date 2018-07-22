a = input('')
l = list(a)
for i in range(len(l)):
    for j in range(i):
        if l[j] > l[i]:
            l[j], l[i] = l[i], l[j]
print (l)
