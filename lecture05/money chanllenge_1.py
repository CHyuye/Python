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


# def main():
#     """"
#     52周存钱挑战
#
#     """
#     total_week = 52  # 总周数(不变值)
#     zhou_shu = 1  # 存钱周数
#     money_per_week = 10  # 每周存钱数
#     increase_money = 10  # 递增金额
#     saving = 0  # 账户累计
#
#     while zhou_shu <= total_week:
#         # 存钱操作
#         saving += money_per_week
#         # 输出信息
#         print('第{}周,存入{}元，账户累计{}元'.format(zhou_shu, money_per_week, saving))
#
#         # 更新下一周的存钱金额
#         money_per_week += increase_money
#         zhou_shu += 1
#
# if __name__ == '__main__':
#     main()
#
import math

saving = 0


def save_money_in_weeks(total_week, per_week_money, increase_money):

    global saving
    money_list = []

    for i in range(total_week):
        money_list.append(per_week_money)
        saving = math.fsum(money_list)

        per_week_money += increase_money
    return saving


def main():

    total_week = int(input('请输入您存储的周数：'))
    per_week_money = float(input('请输入您每周存入的金额：'))
    increase_money = float(input('请输入您每周递增的金额：'))
    saving = save_money_in_weeks(total_week, per_week_money, increase_money)

    print('您的存款金额为：', saving)


if __name__ == '__main__':
    main()

