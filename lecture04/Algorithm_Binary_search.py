"""
    二分查找——只能查找已经排序好的数据
    二分查找通过比较数组中间的数据与目标数据的大小，
    可以得知目标数据在数组的左边还是右边，比较一次范围缩小一次，重复操作

"""

def binary_search(alist, item):
    """二分查找，递归"""
    n = len(alist)
    if n > 0 :
        mid = n //2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False


def binary_search1(alist, item):
    """二分查找，非递归"""
    # 列表的起始索引
    first = 0
    # 列表的最终下标
    last = len(alist) - 1
    # 程序会一直执行，直到二者相同
    while first <= last:
        # 第一次查找
        middle = (first + last) // 2
        # 在列表中查找到索引对应的值
        # guess = list_item[mid]
        # 如果查找到就返回
        if alist[middle] == item:
            return True
        # 如果列表数字大于目标数字，最大索引设置为上一次查找的索引-1
        elif item < alist[middle]:
            low = middle - 1
        # 如果列表数字小于目标数字，最大索引设置为上一次查找的索引+1
        else:
            first = middle + 1
    # 没有查找到就返回空
    return False


if __name__ == '__main__':
    list = [3,9,11,15,19,25,33,34]
    print(binary_search1(list, 15))
    print(binary_search(list, 19))

