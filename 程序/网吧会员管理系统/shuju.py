#输入正确才可进入系统
id_card = []
def show_menu():#显示菜单
    print('*' * 50)
    print('欢迎使网吧管理系统S1.0')
    print('1.新建会员')
    print('2.显示所有会员')
    print('3.搜索会员')
    print('4.删除会员')
    print('5.修改会员')
    print('6.保存会员数据')
    print('7.显示帮助信息')
    print('8.开户上机')
    print('0.退出系统:')
    print('*' * 50)
#普通用户菜单                
def shows_menu():
    print('*' * 50)
    print('欢迎使网吧管理系统S1.0')
    print('1.显示所有会员')
    print('2.搜索会员')
    print('3.显示帮助信息')
    print('0.退出系统:')
    print('*'*50)
def show_help():#显示帮助
    print('只有管理者才可以登录此系统')
    print('此系统由逍遥帅开发')
def new_card():#新建会员
    name = input('请输入姓名:')
    card = input('请输入身份证号码:')
    phone = input('请输入手机号:')
    money = input('请输入充值金额(元):')
    zd = {}
    zd['name'] = name
    zd['card'] = card
    zd['phone'] = phone
    zd['money'] = money
    id_card.append(zd)
def show_card():#显示所有会员
    print('*'*50)
    print('会员信息如下:')
    print('序号  姓名  身份证号码      手机号   预留金额')
    i = 1
    for temp in id_card:
        print('%d   %s    %s   %s  %s'%(i,temp['name'],temp['card'],temp['phone'],temp['money']))
        i += 1
def search_card():#搜索会员
    find_name = input('请输入要查询的名字:')
    for zd in id_card:
        if find_name == zd['name']:
             print('姓名   身份证号码    电话    预留金额')
             print('*' * 30)
             print('%s   %s   %s   %s'%(zd['name'],zd['card'],zd['phone'],zd['money']))
             break
def del_card(member):#删除会员
    del_card = int(input('请输入要删除的会员序号')) - 1
    del member[del_card]
def change_card():#修改会员
    card_id = int(input('请输入修改的会员的序号":'))
    name = input ('请输入新会员的名字:')
    card = input ('请输入新会员身份证号码:')
    phone = input('请输入新会员的手机号:')
    money = input('请输入新会员充值金额(元):')
    id_card[card_id-1]['name'] = name
    id_card[card_id-1]['card'] = card
    id_card[card_id-1]['phone'] = phone
    id_card[card_id-1]['money'] = money
def save_to_file():#保存到本地
    file = open('new_card.data','w')
    file.write(str(id_card))
    file.close()
def recover_data():
    global id_card
    try:
        file = open('new_card.data')
        content = file.read()
        id_card = eval(content)
        file.close()
    except:
        print('没有记录')
def cz_money():#登陆上机
    sj_name = input('请输入上机人姓名')
    for zd  in id_card:
        s = zd['money']
        if sj_name == zd['name']:
            a = input('%s是否需要激活上机？(Yes or No)'%sj_name)
            if a == 'Yes':
                print('欢迎登录，%s的剩余金额为%s(元)'%(sj_name,s))
            else:
                print('欢迎下次再来')

