"""
    作者：陈志安
    功能：判断密码强弱

"""


def check_number_exist(password_str):
    """
        判断字符串中是否含有数字
    """
    has_number = False
    for c in password_str:
        if c.isnumeric():
            has_number = True
            break
    return has_number


def check_letter_exist(password_str):
    """
        判断是否有字母
    """
    has_letter = False
    for c in password_str:
        if c.isalpha():
            has_letter = True
            break
    return has_letter


def main():
    """
        主函数
    """
    # try_time = 5
    #
    # while try_time > 0:
    #     password = input('请输入您的密码：')
    #
    #     # 密码强度
    #     strength_level = 0
    #
    #     # 规则一：8位密码
    #     if len(password) >= 8:
    #         strength_level += 1
    #     else:
    #         print('请输入8位数密码！')
    #
    #     # 规则二：包含数字
    #     if check_number_exist(password):
    #         strength_level += 1
    #     else:
    #         print('请输入带数字的密码!')
    #     # 规则三：包含字母
    #     if check_letter_exist(password):
    #         strength_level += 1
    #     else:
    #         print('请输入带字母的密码')
    #     if strength_level == 3:
    #         print('密码设置成功！')
    #     else:
    #         print('密码强度不合格！')
    #         try_time -= 1
    #     print('------------------------------')
    # if try_time <= 0:
    #     print('尝试次数过多，请稍后再试！')

    f = open('password_3.0.txt', 'r')
    # 1,  read()
    # content = f.read()
    # print(content)

    # 2, readlines()

    for line in f:
        print('read:{}'.format(line))

    f.close()


if __name__ == '__main__':
    main()
