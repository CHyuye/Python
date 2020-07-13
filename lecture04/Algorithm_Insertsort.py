"""
    插入排序--就是从右侧的未排序区域内取出一个数据，然后将它插到已排序区域内合适的位置
"""
import random


def insertsort(a, length):
    for i in range(1, length):
        if a[i-1] > a[i]:
            t = a[i]
            j = i-1
            while a[j] > t and j >= 0:
                a[j+1] = a[j]
                j = j-1
                a[j+1] = t


arr_list = [each for each in range(20)]
random.shuffle(arr_list)
print("随机生成数", arr_list)
insertsort(arr_list, len(arr_list))
print("插入排序后", arr_list)