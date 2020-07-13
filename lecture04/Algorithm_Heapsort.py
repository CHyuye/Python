"""
    堆排序——就是把堆顶的最大数取出来，将剩余堆继续调整为最大堆
"""

import time, random


def adjustHeap(ls, start, end):
    while start * 2 <= end:
        j = start * 2
        if j < end and ls[j] < ls[j+1]:  # 让j指向最大的节点
            j += 1
        if ls[start] < ls[j]:
            ls[start], ls[j] = ls[j], ls[start]
            start = j
        else:
            break


def heapSort(ls):
    n = len(ls)
    ls.insert(0, 0)  # 第一位不用
    for i in range(n//2, 0, -1):  # 初始化堆，使得每个节点都符合堆的要求
        adjustHeap(ls, i, n)
    while n > 1:
        ls[1], ls[n] = ls[n], ls[1]  # 将第一个最大值沉到底部，从而获得最后的升序
        n -= 1
        adjustHeap(ls, 1, n)
    return ls[1:]


def main():
    arr = [each for each in range(200)]
    random.shuffle(arr)
    print("随机生成数", arr)
    start_t = time.time()
    res = heapSort(arr)
    end_t = time.time()
    print("cost:", end_t - start_t)
    print("堆排序后", res)


if __name__ == "__main":
    main()
