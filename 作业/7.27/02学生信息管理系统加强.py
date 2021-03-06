student_infos = []
def print_menu():
    print('*'*50)
    print('学生信息管理系统')
    print('^_^\t' * 10)
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.显示所有学生信息')
    print('5.查询学生信息')
    print('0.退出系统')
    print('*'*50)
def add_info():
    name = input('请输入学生姓名:')
    sex = input('请输入学生性别:')
    phone = input('请输入学生手机号码:')
    print('添加成功')
    new_infos = {}
    new_infos['name'] = name
    new_infos['sex'] = sex
    new_infos['phone'] = phone
    student_infos.append(new_infos)
def del_info(student):
    del_number = int(input('请输入要删除的学生序列号:')) - 1
    del student[del_number]
def change_info():
    student_id = int(input('请输入要修改的学生的序号'))
    name = input ('请输入新学生的名字:')
    sex = input ('请输入新学生的性别:(男/女)')
    phone = input('请输入新学生的手机号:')
    student_infos[student_id-1]['name'] = name
    student_infos[student_id-1]['sex'] = sex
    student_infos[student_id-1]['phone'] = phone
def show_info():
    print('*' * 50)
    print('学生信息如下')
    print('*' * 50)
    print('序号 姓名 性别 手机号')
    i = 1
    for temp in student_infos:
        print('%d  %s  %s  %s'%(i,temp['name'],temp['sex'],temp['phone']))
        i += 1
def search_info():
    find_name = input('请输入要查询学生的名字')
    for new_infos in student_infos:
        if new_infos['name'] == find_name:
            print('姓名 性别 电话')
            print('*' * 30)
            print('%s %s %s'%(new_infos['name'],new_infos['sex'],new_infos['phone']))
def main():
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
            search_info()
        elif key == '0':
            quit_confirm = input('亲，真的要退出么?(Yes or No)')
            if quit_confirm == 'Yes':
                break
            else:
                print('输入有误，请重新输入')
main()
