from time import ctime,sleep
def timefun(func):
    def wra():
        print("%s called at %s" % (func.__name__, ctime()))
        func()
    return wra
@timefun
def q():
    print('111')
q()    
