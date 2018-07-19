card_list=[]
def show_menu():
    print('*'*50)
    print('欢迎使用【名片管理系统】V1.0')
    print('')
    print('1.新建名片')
    print('2.显示全部')
    print('3.查询名片')
    print('')
    print('0.退出系统')
    print('*'*50)
def new_card():
    print('-'*50)
    print('功能:新建名片')
    name = input('请输入姓名：')
    phone = input('请输入电话：')
    qq = input('请输入QQ号码：')
    email = input('请输入邮箱：')
    card_dict = {'name':name,'phone':phone,'qq':qq,'email':email}
    card_list.append(card_dict)
   #print(card_list)
    print('成功添加%s的名片'% card_dict['name'])
def show_all():
    print('-'*50)
    print('功能：显示全部')
    print('姓名\t\t电话\t\tQQ\t\t邮箱')
    print('='*40)
    for card_dict in card_list:
        print('%s\t\t%s\t\t%s\t\t%s'%(card_dict['name'],card_dict['phone'],card_dict['qq'],card_dict['email']))   
    if len(card_list) ==0:
        print('提示没有任何名片记录')
        return        
def search_card():
    print('-'*50)
    print('功能：搜索名片')
    find_name = input('请输入要搜索的名字：')
    for card_dict in card_list:
        if find_name == card_dict['name']:
            print('姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱')
            print('-'*50)
            print('%s\t\t\t%s\t\t\t%s\t\t\t%s'%(card_dict['name'],card_dict['phone'],card_dict['qq'],card_dict['email']))
            deal_card(card_dict)
            break
    else:
        print('没有找到%s'% find_name)
def deal_card(card_dict):
    action = input('请选择要执行的操作[1]修改[2]删除')
    #if action == '1':
        #print('修改')
    #elif action == '2':
        #print('删除')
    if action == '2':
        card_list.remove(card_dict)
        print('删除成功')
    elif action == '1':
        card_dict['name'] = input('请输入要修改名字')
        card_dict['phone'] = input('请输入要修改手机号')
        card_dict['QQ'] = input('请输入要修改的QQ号码')
        card_dict['email'] = input('请输入要修改的电子邮箱:')
        print('修改成功')
       # card_dict['name'] = input('请输入姓名：')
       # card_dict['phone'] = input('请输入电话：')
       # card_dict['qq'] = input('请输入QQ：')
       # card_dict['email'] = input('请输入邮箱：')
       # print('%s的名片修改成功'%card_dict['name'])
'''       
def input_card_info(dict_value,tip_message):
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value   
'''
