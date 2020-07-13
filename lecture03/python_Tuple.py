"""
    元组与列表类似，不同之处在于元组的【元素不可以修改】
    元组 —— 表示多个元素组成的序列
    元组有特定的应用场景
    用于存储一串信息，数据之间使用','分割
    元组用()定义
"""

# 索引就是数据元组的编号
#
info_tuple = ("郑三", 18, 1.70)
#
# # 空元祖
# empty_tuple = ()  # 创建空元组后不能修改
#
# # 元组只包含一个元素时，需要在元素后面添加逗号
# single_tuple = (12,)

# 1.取值和取索引
# print(info_tuple[0])
#
# # 取索引是已经知道数据内容，希望知道数据位置
# print(info_tuple.index(1.70))
#
# # 2.统计计数
# print(info_tuple.count(18))
#
# # 统计元祖包含元素个数
# print(len(info_tuple))

# 元组的循环遍历
# for my_info in info_tuple:
#
#     # 使用格式字符串拼接my_info这个变量不方便
#     # 因为元组中通常保存的数据类型是不同的！
#     print(my_info, end=" ")


# 应用场景
"""
    1.函数的参数和返回值，一个函数可以接受多个参数，或者一次返回多个数据
    2.格式字符串，格式化字符串后面的()本质上就是元组
    3.让列表不可以修改，以保护数据安全
"""

# 格式字符串，格式化字符串后面的()本质上就是元组
print("我是%s,年龄%d,身高%.2f" % info_tuple)

info_str = "我是%s,年龄%d,身高%.2f" % info_tuple

print(info_str)


# 元组和列表之间类型的转换
num_list = [1, 3, 5, 7, 9]

num_tuple = tuple(num_list)

num2_list = list(num_tuple)
