student_infos = []
def print_menu():#显示菜单
    print('*'*50)
    print('学生信息管理系统')
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.显示所有学生信息')
    print('5.保存数据')
    print('0.退出系统')
    print('*'*50)
def add_info():#添加学生信息
    name = input('请输入学生姓名:')
    sex = input('请输入学生性别:')
    phone = input('请输入学生手机号码:')
    print('添加成功')
    new_infos = {}
    new_infos['name'] = name
    new_infos['sex'] = sex
    new_infos['phone'] = phone
    student_infos.append(new_infos)
def del_info(student_infos):#删除信息
    del_number = int(input('请输入要删除的学生序列号:')) - 1
    del student_infos[del_number]
def change_info():#修改学生信息
    student_id = int(input('请输入要修改的学生的序号:'))
    name = input ('请输入新学生的名字:')
    sex = input ('请输入新学生的性别:(男/女)')
    phone = input('请输入新学生的手机号:')
    student_infos[student_id-1]['name'] = name
    student_infos[student_id-1]['sex'] = sex
    student_infos[student_id-1]['phone'] = phone
def show_info():#展示所有学生信息
    print('*' * 50)
    print('学生信息如下')
    print('*' * 50)
    print('序号 姓名 性别 手机号')
    i = 1
    for temp in student_infos:
        print('%d  %s  %s  %s'%(i,temp['name'],temp['sex'],temp['phone']))
        i += 1
def save_to_file():
    file = open('student.data','w')
    file.write(str(student_infos))
    file.close()
def recover_data():
    global student_infos
    try:
        file = open('student.data')
        content = file.read()
        student_infos = eval(content)
        file.close()
    except:
        print('没有历史记录')
def main():
    recover_data()
    while True:
        print_menu()
        key = input('请输入对应的编号')
        if key == '1':
            add_info()
        elif key == '2':
            del_info(student_infos)
        elif key == '3':
            change_info()
        elif key == '4':
            show_info()
        elif key == '5':
            save_to_file()
        elif key == '0':
            quit_confirm = input('亲，真的要退出么?(Yes or No)')
            if quit_confirm == 'Yes':
                break
            else:
                print('输入有误，请重新输入')
main()
