"""
    线性查找——从待查找的数据中的第一个元素开始，逐个对比
"""


def Liner(values, key):
    length = len(values)
    for i in range(length):
        if values[i] == key:
            return "查找成功:%d" % i

    else:
        return "查找失败!"


if __name__ == '__main__':
    values = [8,10,30,22,80,45,19]
    print(Liner(values, 45))