import cards_tools
while True:
    cards_tools.show_menu()
    action = input('请选择操作功能:')
    print('你选择的操作是:%s'%action)
    if action in ['1','2','3']:
        if action == '1':
            cards_tools.new_card()
        elif action == '2':
            cards_tools.show_all()
        elif action == '3':
            cards_tools.search_card()      
    elif action == '0':
        print('欢迎再次使用【名片管理系统和】')
        break
    else:
        print('输入有误，请重新输入')

