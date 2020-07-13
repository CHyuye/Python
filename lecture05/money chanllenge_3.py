""""
    作者：陈志安
    功能：52周存钱挑战
"""
import math

# 全局变量
saving = 0


# def save_money_in_weeks(total_week, per_money_week, increase_money):
#     """"
#         计算n周内的存款金额
#     """
#     global saving  # 使变量全局化
#     money_list = []
#
#     for i in range(total_week):
#         money_list.append(per_money_week)
#         saving = math.fsum(money_list)
#
#         # print('第{}周,存入{}元,账户累计{}元'.format(i + 1, per_money_week, saving))
#         per_money_week += increase_money
#
#     return saving


def save_money_in_weeks(total_week, per_money_week, increase_money):
    """
    52周存钱挑战
    :param total_week:总周数
    :param per_money_week: 每周存多少
    :param increase_money: 每周递增金额
    :return: 总存储金额
    """
    global saving
    money_list = []  # 存钱列表[10, 20, 30]

    for i in range(total_week):
        money_list.append(per_money_week)
        saving = math.fsum(money_list)

        per_money_week += increase_money

    return saving


def main():

    per_money_week = float(input('请输入每周的存入金额：'))
    total_week = int(input('请输入总共的周数：'))
    increase_money = float(input('请输入每周的递增金额：'))

    # 调用函数
    saving = save_money_in_weeks(total_week, per_money_week, increase_money)

    print('总存款金额：', saving)


if __name__ == '__main__':
    main()
