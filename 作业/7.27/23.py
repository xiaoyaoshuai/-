def w(func):
    def inner():
        print('正在验证')
        func()
    return inner
@w
def Test():
    print('哈哈')
Test()
