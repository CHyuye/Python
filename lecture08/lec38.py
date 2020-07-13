"""
    作者：陈志安
    日期：19.03.18
    功能：模拟投掷骰子
    v.2：同时投掷两个骰子
    v.3:可视化投掷两个骰子结果
"""

import random
import matplotlib.pylab as plt


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
    total_times = 100
    # 初始化列表 result_list = [0,0,0,0,0,0]
    result_list = [0] * 11

    # 初始化点数列表
    roll_list = list(range(2, 13))
    roll_dict = dict(zip(roll_list, result_list))

    # 记录骰子的结果
    roll_a_list = []
    roll_b_list = []

    for i in range(total_times):
        roll_a = roll_dice()
        roll_b = roll_dice()

        roll_a_list.append(roll_a)
        roll_b_list.append(roll_b)

        for j in range(2, 13):
            if (roll_a + roll_b) == j:
                roll_dict[j] += 1

    for i, result in roll_dict.items():
        print('点数{}的次数:{}，频率为{}'.format(i, result, result/total_times))

    # 数据可视化
    x = range(1, total_times + 1)
    plt.scatter(x, roll_a_list, c='red', alpha=0.5)
    plt.scatter(x, roll_b_list, c='green', alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()
