import shuju
def pt(fun):
    def kv():
        print('普通用户')
        fun()
    return kv
@pt
def main1():
    shuju.recover_data()
    while True:
        shuju.shows_menu()
        key = input('请输入你的选择')
        if key == '1':
            shuju.show_card()
        elif key == '2':
            shuju.search_card()
        elif key == '3':
            shuju.show_help()
        elif key == '0':
            quit = input('亲，真的要退出么?:(Yes or No)')
            if quit == 'Yes':
                print('已退出')
                break
