"""
    作者：陈志安
    日期：19.03.18
    功能：模拟投掷骰子
    v.2：同时投掷两个骰子
    v.3:可视化投掷两个骰子结果
    v.4:数据直方图
"""

import random
import matplotlib.pylab as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


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
    total_time = 10000
    # 记录骰子的结果
    roll_list = []

    for i in range(total_time):
        roll_one = roll_dice()
        roll_two = roll_dice()

        roll_list.append(roll_one + roll_two)

    # 数据可视化
    plt.hist(roll_list, bins=range(2, 14), normed=1, edgecolor='black', linewidth=1)
    plt.show()


if __name__ == '__main__':
    main()
