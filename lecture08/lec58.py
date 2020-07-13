"""
    作者：陈志安
    日期：19.03.18
    功能：模拟投掷骰子
    v.2：同时投掷两个骰子
    v.3:可视化投掷两个骰子结果
    v.4:数据直方图
    v.5:科学计算法
"""
import numpy as np
import matplotlib.pylab as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    total_times = 1000
    # 记录骰子的结果
    roll_one_arr = np.random.randint(1, 7, size=total_times)
    roll_two_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll_one_arr + roll_two_arr

    hist, bins = np.histogram(result_arr, bins=range(2, 14))
    print(hist)
    print(bins)

    # 数据可视化
    plt.hist(result_arr, bins=range(2, 14), normed=1, edgecolor='black', linewidth=1, rwidth=0.8)

    # 设置X轴坐标点显示
    tick_labels = ['2点', '3点', '4点', '5点',
                   '6点', '7点', '8点', '9点',
                   '10点', '11点', '12点', ]
    tick_pos = np.arange(2, 13) + 0.5
    plt.xticks(tick_pos, tick_labels)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()
