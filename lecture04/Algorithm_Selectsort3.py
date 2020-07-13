
"""
    选择排序算法三：优化版，思路每次分别找到最小值和最大值放到列表头部和尾部
"""

import random


def select_sort(arr):
    for i in range(len(arr) - 1):
        min_position = i
        max_position = i
        for j in range(i+1, len(arr) - i):
            min_position = j if arr[min_position] > arr[j] else min_position
            max_position = max_position if arr[max_position] > arr[j] else j
        if arr[min_position] < arr[max_position]:
            print([min_position, max_position])
            start_pos = arr[i]
            arr[i] = arr[min_position]
            arr[min_position] = start_pos
            for jj in range(i+1, len(arr) - i):
                max_position = max_position if arr[max_position] > arr[jj] else jj
            end_pos = arr[-i - 1]
            arr[-i - 1] = arr[max_position]
            arr[max_position] = end_pos
            print("循环结果", arr)


if __name__ == "__main__":
    arr_list = [each for each in range(20)]
    random.shuffle(arr_list)
    print("生成随机数", arr_list)
    select_sort(arr_list)
    print("选择排序后", arr_list)



