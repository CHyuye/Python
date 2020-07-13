# 字符串类型不能相乘，需要转换为浮点数或者为整数
# 1.输入苹果的价格
# price = float(input("请输入苹果的价格(单位：元/斤）："))
#
# # 2.要求苹果的重量
# weight = float(input("请输入苹果的重量(单位：斤)："))
#
# # # 3.计算金额
# # price = float(price_str)
# #
# # weight = float(weight_str)
#
# money = price * weight
# # %.2f 表示保留小数点2位
# print("苹果单价 %.2f 元/斤，购买了 %.2f 斤，需要 %.2f 元" % (price, weight, money))

"""
    %s -- 字符串
    %d -- 有符号十进制整数，%06d表示显示位数不足用0补全
    %f -- 浮点数，%.2f表示显示两位数
    %% -- 输出%
"""
#
# name = "陈寒"
# # print("我的名字叫%s,请多多关照！" % name)
#
# # %09d 表示没有到9位数就在前面增加0
# student_ID = 18213023
# print("我的名字叫%s，我的学号是%09d，请多多关照！" % (name, student_ID))
#
# # 浮点数小数 %%表示有一个%
# scale = 0.25
# print("数据比例是 %.2f%%" % (scale * 100))


# # 冒泡排序
# import time
#
#
# # 第一种野路子冒泡排序
# def Bubblesort1(array):
#     time1_start = time.time()
#     length = len(array)
#     while length > 1:
#         for i in range(length - 1):
#             if array[i] > array[i+1]:
#                 array[i], array[i+2] = array[i+1], array[i+1]
#         length -= 1
#     # print(array)
#     time1_end = time.time()
#     print(time1_end - time1_start)
#
#
# # 正常排序无优化
# def Bubblesort2(array):
#     time2_start = time.time()
#     length = len(array)
#     for i in range(length)[::-1]:
#         for j in range(i):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#
#     time2_end = time.time()
#     print(time2_end - time2_start)
#
#
# # 冒泡排序有优化，设置交换符号
# def Bubblesort3(array):
#     time3_start = time.time()
#     length = len(array)
#     for i in range(length)[::-1]:  [::-1] 数据逆序
#         flag = False  # 先假设未作交换操作
#         for j in range(i):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#                 flag = True  # 设置交换标志
#         if not flag:
#             break   # 无交换操作，表示已完成排序，退出循环
#     time3_end = time.time()
#     print(time3_end - time3_start)
#
#
# # 双向冒泡（鸡尾酒排序）因为未发生交换操作的区域是有序的，故每轮扫描下来可以可以更新上下边界，减少扫描范围
# def Bubblesort4(array):
#     low, high = 0, len(array - 1)
#     while low > high:
#         swapFlah = low  # 先假设最后一次发生交换操作的位置是low
#         for j in range(low, high):  # 顺序扫描A[low..high-1]
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#                 swapFlah = j
#         high = swapFlah  # 修改待排序数组的上界为最后一次发生交换操作的位置
#         for j in range(high, low-1):  # 逆序扫描[high..low-1]
#             if array[j] < array[j+1]:
#                 array[j], array[j-1] = array[j-1], array[j]
#                 swapFlah = j
#         low = swapFlah   # 修改待排序数组的下界为最后一次发生交换操作的为位置
#
#
#
# list = [3,2,4,9,10,14,33,23,90,19,29] + list(range(12,1000))
# Bubblesort1(list)
# print('------------------------------')
# Bubblesort2(list)
# print('------------------------------')
# Bubblesort3(list)

