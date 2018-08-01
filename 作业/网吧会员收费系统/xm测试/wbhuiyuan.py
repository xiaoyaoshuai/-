'''
网吧会员登录管理系统
结账下机功能未实现
'''
#存储会员信息
id_card = []
#普通用户
def main1():
    recover_data()
    while True:
        shows_menu()
        key = input('请输入你要选择的功能:')
        if key == '1':
            show_card()
        elif key == '2':
            search_card()
        elif key == '3':
            show_help()
        elif key == '0':
            quit = input('亲，真的要退出么?:(Yes or No)')
            if quit == 'Yes':
                print('已退出')
                break
            elif quit == 'No':
                print('请继续使用')
            else:
                print('输入有误')
#管理者程序
def main():
    recover_data()
    while True:
        show_menu()
        key = input('请输入你要选择的功能:')
        if key == '1':
            new_card()
        elif key == '2':
            show_card()
        elif key == '3':
            search_card()
        elif key == '4':
           del_card(id_card)
        elif key == '5':
            change_card()
        elif key == '6':
            save_to_file()
        elif key == '7':
            show_help()
        elif key == '8':
            cz_money()
        elif key == '0':
            quit = input('亲，真的要退出么?:(Yes or No)')
            if quit == 'Yes':
                print('已退出')
                break
            elif quit == 'No':
                print('请继续使用')
            else:
                print('输入有误')
#普通用户菜单                
def shows_menu():
    print('*' * 50)
    print('欢迎使网吧管理系统S1.0')
    print('1.显示所有会员')
    print('2.搜索会员')
    print('3.显示帮助信息')
    print('0.退出系统:')
    print('*'*50)
#管理者菜单
def show_menu():
    print('*' * 50)
    print('欢迎使网吧管理系统S1.0')
    print('1.新建会员')
    print('2.显示所有会员')
    print('3.搜索会员')
    print('4.删除会员')
    print('5.修改会员')
    print('6.保存会员数据')
    print('7.显示帮助信息')
    print('8.激活上机')
    print('0.退出系统:')
    print('*' * 50)
#显示帮助系统
def show_help():#
    print('='* 40)
    print('')
    print('此系统主要用于网吧会员管理')
    print('此系统由逍遥帅开发')
    print('有问题请联系作者')
    print('')
    print('='* 40)
#新建会员
def new_card():
    name = input('请输入姓名:')
    card = input('请输入身份证号码:')
    phone = input('请输入手机号:')
    money = int(input('请输入充值金额(元):'))
    zd = {}
    zd['name'] = name
    zd['card'] = card
    zd['phone'] = phone
    zd['money'] = money
    id_card.append(zd)
#显示会员
def show_card():
    print('*'*50)
    print('会员信息如下:')
    print('序号  姓名  身份证号码  手机号   余额(元)')
    print('*'*50)
    i = 1
    for temp in id_card:
        print('%d   %s    %s   %s  %s'%(i,temp['name'],temp['card'],temp['phone'],temp['money']))
        i += 1
#删除会员
def search_card():
    find_name = input('请输入要查询的名字:')
    for zd in id_card:
        if find_name == zd['name']:
             print('姓名   身份证号码   电话    余额(元)')
             print('*' * 50)
             print('%s   %s   %s   %d'%(zd['name'],zd['card'],zd['phone'],zd['money']))
             break
#登录上机
def cz_money():
    sj_name = input('请输入上机人姓名')
    for zd  in id_card:
        s = zd['money']
        if sj_name == zd['name']:
            a = input('%s是否需要激活上机？(Yes or No)'%sj_name)
            if a == 'Yes':
                print('欢迎登录，%s的剩余金额为%s(元)'%(sj_name,s))
            else:
                print('欢迎下次再来')
#删除会员
def del_card(member):
    print('删除会员')
    del_card = int(input('请输入要删除的会员序号')) - 1
    c = input('您确定要删除此会员么？(Yes or No)')
    if c == 'Yes':
        del member[del_card]
    elif c == 'No':
        print('已退出')
    else:
        print('输入有误')
#修改会员
def change_card():
    card_id = int(input('请输入修改的会员的序号":'))
    name = input ('请输入新会员的名字:')
    card = input ('请输入新会员身份证号码:')
    phone = input('请输入新会员的手机号:')
    money = int(input('请输入新会员的充值金额'))
    id_card[card_id-1]['name'] = name
    id_card[card_id-1]['card'] = card
    id_card[card_id-1]['phone'] = phone
    id_card[card_id-1]['money'] = money
#管理者保存
def save_to_file():
    file = open('card.data','w')
    file.write(str(id_card))
    file.close()
#查看文件    
def recover_data():
    global id_card
    try:
        file = open('card.data')
        content = file.read()
        id_card = eval(content)
        file.close()
    except:
        print('没有记录')


