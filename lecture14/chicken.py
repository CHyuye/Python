"""
求解《白钱百鸡》问题
1只公鸡5元，1只母鸡3元，3只小鸡1元，用100元买100只鸡
问能买公鸡，母鸡，小鸡各多少只？
Author：Eidit
Date:19/5/6
"""

# for x in range(1, 20):
#     for y in range(1, 33):
#         z = 100 - x - y
#         if 5*x + 3*y + z/3 == 100:
#             print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (x, y, z))

from math import log2, factorial
from matplotlib import pyplot

import numpy


# noinspection PyInterpreter,PyInterpreter
def seq_search(items: list, elem)->int:
    """顺序查找"""
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1


def bin_search(items, elem):
    """二分查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem > items[mid]:
            start = mid + 1
        elif elem < items[mid]:
            start = mid - 1
        else:
            return mid
    return -1


def main():
    """主函数（入口）"""
    num = 6
    styles = ['r-.', 'g-*', 'b-o', 'y-x', 'c-^', 'm-+', 'k-d']
    legends = ['对数', '线性', '线性对数', '平方', '立方', '几何级数', '阶乘']
    x_data = [x for x in range(1, num + 1)]
    y_data1 = [log2(y) for y in range(1, num + 1)]
    y_data2 = [y for y in range(1, num + 1)]
    y_data3 = [y * log2(y) for y in range(1, num + 1)]
    y_data4 = [y ** 2 for y in range(1, num + 1)]
    y_data5 = [y ** 3 for y in range(1, num + 1)]
    y_data6 = [3 ** y for y in range(1, num + 1)]
    y_data7 = [factorial(y) for y in range(1, num + 1)]
    y_datas = [y_data1, y_data2, y_data3, y_data4, y_data5, y_data6, y_data7]
    for index, y_data in enumerate(y_datas):
        pyplot.plot(x_data, y_data, styles[index])
    pyplot.legend(legends)
    pyplot.xticks(numpy.arange(1, 7, step=1))
    pyplot.yticks(numpy.arange(0, 751, step=50))
    pyplot.show()

if __name__ == '__main__':
    main()

