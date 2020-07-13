# 存储所有字典数据
card_list = []


def show_menu():

    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V 1.0\n")
    print("1. 新增名片")
    print("2. 显示名片")
    print("3. 查询名片\n")
    print("0. 退出程序")
    print("*" * 50)


def new_card():

    """新增名片"""
    print("=" * 50)
    print("功能：|新增名片|\n")

    # 1.提示用户输入信息
    # shift + F6 重命名变量
    name_str = input("请输入您的姓名：")
    phone_str = input("请输入您的手机号：")
    qq_str = input("请输入您的QQ：")
    email_str = input("请输入您的邮箱：")

    # 2.使用用户输入的信息建立字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3.将字典信息加列表中
    card_list.append(card_dict)
    print(card_list)

    # 4.提示添加成功
    print("您成功添加 %s 的名片信息！" % name_str)


def show_all():

    """显示所有名片"""
    print("=" * 50)
    print("功能：|显示名片|\n")

    # 判断是否存在名片记录，如果没有，提示用户返回
    if len(card_list) == 0:

        print("当前还未添加名片信息，请使用新增名片功能！\n")
        # return 可以返回一个函数的执行结果
        # 下方代码不会被执行
        # return后面如没任何结果，表示返回到调用函数的位置，并且不返回结果
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t\t")

    print("")
    # 打印分割线
    print("-" * 50)

    # 遍历所有名片列表依次输出字典信息
    for card_dict in card_list:

        print("%s\t\t%s  \t\t%s\t\t%s" % (card_dict["name"],
                                          card_dict["phone"],
                                          card_dict["qq"],
                                          card_dict["email"]))
    print("")


def search_card():

    """搜索名片"""
    print("=" * 50)
    print("功能：|查询名片|\n")
    # 1.提示用户输入搜索姓名

    find_name = input("请输入您要查询的姓名：")

    # 2.遍历名片列表，查询搜索的姓名，如没找到，提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
            print("-" * 50)
            print("%s \t\t%s \t\t%s \t\t%s" % (card_dict["name"],
                                               card_dict["phone"],
                                               card_dict["qq"],
                                               card_dict["email"]))
            print("")
            # 针对找到名片执行修改和删除的操作
            deal_card(card_dict)
            break
    else:
        print("抱歉，没有找到您要查询的 %s" % find_name)


def deal_card(find_dict):
    """
        处理查找到的名片信息
    :param find_dict: 查找到的名片
    """
    action_str = input("请选择要执行的操作"
                        "[R] 修改 [D] 删除 [Q] 返回")

    if action_str == "R":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ:")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")

        print("修改名片成功！\n")

    elif action_str == "D":
        card_list.remove(find_dict)
        print("删除名片成功！\n")


def input_card_info(dict_value, tip_message):
    """
        输入名片信息
    :param dict_value: 字典原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入内容，就返回内容，否则返回原有字典值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)

    # 2.针对用户输入的内容进行判断，如果用户输入内容，就直接返回
    if len(result_str) > 0:
        return result_str

    # 3.如果用户没有修改内容，就返回‘字典原有内容’
    else:
        return dict_value
