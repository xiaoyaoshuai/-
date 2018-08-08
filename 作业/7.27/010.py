def out(a,b):
    def inner(x):
        if a > b:
            return a*x
        else:
            return b*x
    return inner
l = out(9,6)
print(l(6))
            
