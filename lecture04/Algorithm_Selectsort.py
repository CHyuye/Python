"""
    选择排序算法一：记录最小值，变换位置
"""
import random


# 找到最小的值
def get_min(arg):
    result = arg[0]
    for i in range(len(arg)):
        if result > arg[i]:
            result = arg[i]
    return result


# 选择排序
def Select_sort(arr):
    for i in range(len(arr)):
        min_value = get_min(arr[i:])
        if arr[i] > min_value:
            arr[arr.index(min_value)] = arr[i]
            arr[i] = min_value
            print("遍历过程中", arr)
    return arr


if __name__ == "__main__":
    arr_list = [each for each in range(20)]
    random.shuffle(arr_list)
    print("生成随机数：", arr_list)

    Select_sort(arr_list)
    print("选择排序后", arr_list)

