"""
    归并排序——把序列分成长度相同的；两个子序列，当无法继续分下去是，就对子序列归并
    归并指的是把两个排好序的子序列合并成一个有序序列
"""
# 该代码有错误，未实现
def Merge(a, p, q, r):
    leftArray = []
    rightArray = []
    n1 = q-p+1+1
    n2 = r-q+1
    for num in range(1,n1):
        index = num+p-1
        leftArray.append(a[index])
    leftArray.append(float("inf"))
    for num in range(1,n2):
        index = num+q
        rightArray.append(a[index])
    rightArray.append(float("inf"))
    i = 0
    j = 0
    print(leftArray)
    print(rightArray)
    for k in range(p, r+1):
        if (leftArray[i] <= rightArray[j]):
            a[k] = leftArray
            i = i + 1
        else:
            a[k] = rightArray[j]
            j = j + 1
    print(a)


def Merge_sort(a,p,r):
    if (p < r):
        q = int((p+r)/2)
        Merge_sort(a, p, q)
        Merge_sort(a, q+1, r)
        Merge(a, p, q, r)


if __name__ == "__main__":
    a = [2, 3, 9, 8,20,10,7]
    Merge_sort(a,0,7)
    print(a)