import shuju
def ws(fun):
    def kf():
        i =1
        while i<=3:
            zh = input('请输入账号')
            pwd = input('请输入密码')
            zh1 = 'xiaoyao'
            pwd1 = '1101'
            if zh == zh1 and pwd == pwd1:
                print('登陆成功')
                fun()
                break
            else:
                print('密码输入错误，请重试')
            i += 1
        if i == 4:
            print('输入次数过多，电脑将自动锁')
    return kf
@ws    
def main():#运行
    shuju.recover_data()
    while True:
        shuju.show_menu()
        key = input('请输入你要选择的功能:')
        if key == '1':
            shuju.new_card()
        elif key == '2':
            shuju.show_card()
        elif key == '3':
            shuju.search_card()
        elif key == '4':
            shuju.del_card(shuju.id_card)
        elif key == '5':
            shuju.change_card()
        elif key == '6':
            shuju.save_to_file()
        elif key == '7':
            shuju.show_help()
        elif key == '8':
            shuju.cz_money()
        elif key == '0':
            quit = input('亲，真的要退出么?:(Yes or No)')
            if quit == 'Yes':
                print('已退出')
                break


