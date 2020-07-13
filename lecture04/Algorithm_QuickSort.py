import random
"""
    快速排序——首先会在序列中选择一个基准值（pivot），然后将除了基准值以外的数分为
    "比基准值大的数"和"比基准值小的数"，再将其排列
"""

data = [45,3,9,15,67,51,42]
def quickSort(data, start, end):
    i = start
    j = end
    # i和j重合时，依次排序结束
    if i >= j:
        return
    # 设置最左边的数为基准值
    flag = data[start]
    while i < j:
        while i < j and data[j] >= flag:
            j -= 1
        # 找到右边的第一个小于基准值的数，赋值给左边的i，此时左边的i被记录在flag中
        data[i] = data[j]
        while i < j and data[i] < flag:
            i += 1
        # 找到左边第一个大于基准值的数，赋值给右边的j，右边的j与左边的i相同
        data[i] = data[j]

    # 由于循环以i结尾，循环完毕后把flag值放在i所在的位置
    data[i] = flag
    # 除去i之外的两端递归
    quickSort(data, start, i-1)
    quickSort(data, i+1, end)


# if __name__ == "__main__":
#     data = [each for each in range(15)]
#     random.shuffle(data)
quickSort(data, 0, len(data) - 1)
print(data)
