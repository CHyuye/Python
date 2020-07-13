"""
    作者：陈志安
    日期：19.03.18
    功能：模拟投掷骰子
    v.2：同时投掷两个骰子
"""

import random


def roll_dice():
    """
        模拟投掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    """
        主函数
    """
    total_times = 1000
    # 初始化列表 result_list = [0,0,0,0,0,0]
    result_list = [0] * 11  # 摇两次色子的总点数

    # 初始化点数列表
    roll_list = list(range(2, 13))  # 从1-12点
    roll_dict = dict(zip(roll_list, result_list))

    for i in range(total_times):
        roll_a = roll_dice()  # 第一次点数
        roll_b = roll_dice()  # 第二次点数

        for j in range(2, 13):
            if (roll_a + roll_b) == j:
                # roll_dict的键是j【点数】 值+1
                roll_dict[j] += 1

    for i, result in roll_dict.items():
        print('点数{}的次数:{}，频率为{}'.format(i, result, result/total_times))
    # 九九乘法表
    # for i in range(1, 10):
    #     for j in range(1, i+1):
    #         print('%d * %d = %d \t'%(i, j, i * j), end='')
    #     print()
    print(roll_dict)


if __name__ == '__main__':
    main()
