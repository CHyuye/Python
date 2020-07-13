
"""
    选择排序算法二：记录最小值的位置，变换值
"""
import random


def select_sort(arr):
    for i in range(len(arr) - 1):
        min_position = i
        for j in range(i+1, len(arr)):
            min_position = j if arr[min_position] > arr[j] else min_position
        swap_pos(arr, i, min_position)
        print("循环结果", arr)


def swap_pos(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


if __name__ == "__main__":
    arr_list = [each for each in range(20)]
    random.shuffle(arr_list)
    print("生成随机数", arr_list)

    select_sort(arr_list)
    print("选择排序后", arr_list)