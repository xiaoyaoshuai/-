import wbhuiyuan
def input_ct():
    d = input('请输入您的身份：1.管理者 or 2.普通用户:')
    if d == '1':
        print('请您进行登录')
        i = 1 
        while i <= 3:
            zh1 = input('请输入账号:')
            pwd1 = input('请输入密码:')
            zh = 'xiaoyao'
            pwd = '1101'
            if zh == zh1 and pwd == pwd1:
                print('登陆成功')
                wbhuiyuan.main()
                break
            else:
                print('账号或密码错误，请重试')
            i += 1
            if i == 4:
                print('次数过多，已退出')
    elif d == '2':
        print('普通用户权限')
        print('')
        print('='*50)
        print('您是普通用户:')
        print('普通用户只能使用搜索会员,显示全部会员和退出功能')
        print('='*50)
        wbhuiyuan.main1()
    else:
        print('输入有误，已退出')

input_ct()
