# 声明全局变量
info = []


# 定义功能界面函数
def print_info():
    print("欢迎来到学员管理系统—————————————————————")
    print("1.添加学员")
    print("2.删除学员")
    print("3.修改学员信息")
    print("4.查询学员信息")
    print("5.显示全部学员信息")
    print("6.退出系统")
    print('—' * 37)


# 1.添加学员的功能函数
def add_stu():
    """添加学员"""
    # 获取新学员的信息
    new_name = input('请输入学员的姓名:')
    new_id = input('请输入学员的学号:')
    new_tel = input('请输入学员的手机号:')

    # 声明全局变量
    global info

    # 判断该学员是否已经存在于该系统中
    for i in info:
        if new_name == i['name']:
            print('该用户已经存在')
            return

    # 定义一个空字典用来添加学员信息
    new_dict = {'name': new_name, 'id': new_id, 'tel': new_tel}

    # 将该字典
    info.append(new_dict)
    print(info)

# 2.删除学员
def del_stu():
    """删除学员"""
    del_name = input('请输入要删除学员的姓名:')

    # 声明全局变量
    global info
    # 查找该学员信息
    for i in info:
        if i['name'] == del_name:
            info.remove(i)
            break
    else:
        print('该用户不存在，请核对您输入的信息')

    print(info)


# 3. 修改学员信息
def modify_stu():
    """修改学员信息"""
    modify_name = input('请输入要修改学员信息的姓名:')

    # 声明全局变量
    global info

    # 查找该学员信息
    for i in info:
        if i['name'] == modify_name:
            i['id'] = input('请输入你要修改的id:')
            i['tel'] = input("请输入你要修改的手机号:")
            break
    else:
        print('该用户不存在，请核对您输入的信息')

    print(info)

# 4. 查询学员信息
def search_stu():
    """"查询学员信息"""
    search_name = input('请输入要查新学员信息的姓名:')

    # 声明全局变量
    global info

    # 查找该学员信息
    for i in info:
        if i['name'] == search_name:
            print('已经找到该学员-------------')
            print(f"该学员的姓名为{i['name']}，学号为{i['id']},手机号为{i['tel']}")
            break
    else:
        print('该用户不存在，请核对您输入的信息')

# 5. 打印所有学员信息
def find_all_stu():
    """显示所有学员信息"""
    print('name\tid\t\ttel')

    # 查找该学员信息
    for i in info:
        print(f"{i['name']}\t{i['id']}\t{i['tel']}")


while True:
    # 1.显示功能界面
    print_info()
    # 2.用户输入功能序号
    Use_Num = int(input("请输入您需要的功能序号:"))
    # 3.根据序号，实现对应功能
    if Use_Num == 1:                            # 1.添加学员
        add_stu()
    elif Use_Num == 2:                          # 2.删除学员
        del_stu()
    elif Use_Num == 3:                          # 3.修改学员信息
        modify_stu()
    elif Use_Num == 4:                          # 4.查询学员信息
        search_stu()
    elif Use_Num == 5:                          # 5.查看所有学员信息
        find_all_stu()
    elif Use_Num == 6:                          # 6.退出系统
        exit_sys = input('确定需要退出吗？ Yes or No')
        if exit_sys == 'Yes':
            break
    else:
        print('您输入的按键有误，请您重新输入')
