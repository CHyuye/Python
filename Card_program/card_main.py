import card_tools
# 无限循环，由客户主动选择退出
while True:

    # TODO注释，用于标记需要去做的工作
    # TODO(Allen) 显示功能菜单
    card_tools.show_menu()

    action_str = input("请选择您要执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1.针对1，2，3的操作
    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            card_tools.new_card()

        # 显示全部
        elif action_str == "2":
            card_tools.show_all()

        # 查询名片
        elif action_str == "3":
            card_tools.search_card()

    # 2. 退出程序0
    elif action_str == "0":
        print("欢迎您再次使用【名片管理系统】")
        break

    # 3. 其他操作，提示错误
    else:
        print("您选择的操作有误，请重新选择！")
