""""
    作者：陈志安
    功能：52周存钱挑战
"""


# def main():
#     """
#         复习上次的BRM
#     """
#     y_or_n = input('是否退出程序，退出请按y，进入请按n')
#     while y_or_n != 'y':
#
#         print('请输入一下信息，并用空格分隔')
#         input_str = input('性别 体重(Kg) 身高(CM) 年龄(岁)：')
#         str_list = input_str.split(' ')
#         gender = str_list[0]
#         weight = float(str_list[1])
#         height = float(str_list[2])
#         age = int(str_list[3])
#
#         if gender == '男':
#             bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
#
#         elif gender == '女':
#             bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
#
#         else:
#             bmr = -1
#
#         if bmr != -1:
#             print('您的性别{},体重{}，身高{}，年龄{}'.format(gender, weight, height, age))
#             print('你的基础代谢率为{}'.format(bmr))
#         else:
#             print('该系统暂不支持，谢谢！')
#
#     print('是否退出程序,退出请按y，继续请按n')
#
#     if y_or_n == 'y':
#         print('程序已退出，谢谢使用！')
#
# if __name__ == '__main__':
#     main()

import math


def main():
    """"
    52周存钱挑战

    """
    total_week = 52
    money_per_week = 10
    per_week = 1
    increase_money = 10
    saving_money = 0

    money_list = []  # 记录每周存款数的列表

    while per_week <= total_week:

        money_list.append(money_per_week)
        saving_money = math.fsum(money_list)

        print('第{}周，存入{}元，账户累计{}'.format(per_week, money_per_week, saving_money))

        money_per_week += increase_money
        per_week += 1


if __name__ == '__main__':
    main()

