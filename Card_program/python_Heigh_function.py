# 函数参数和返回值的作用
"""
    1、如果函数内部处理的数据不稳定，就可以将外界的数据以参数的形势传递到函数内部
    2、如果希望一个函数执行完成后，向外界汇报执行结果，就可以增加函数的返回值

    函数 —— 一个封装独立的代码，在需要时通过函数名调用 可以访问全局变量
    参数 —— 外界希望在函数内部处理的数据
    返回值 —— 向外界报告函数的执行结果
"""

# （1）函数的返回值


# def measure():
#
#     """测量温度和湿度"""
#     print("测量开始···")
#     temp = 35
#     wetness = 60
#     print("测量结束···")
#
#     # 元组——可以包含多个值，用元组返回多个值
#     # return (temp, wetness)
#     return temp, wetness  # 元组，可以省略小括号
#
#
# result = measure()
# print(result)
#
# # 单独处理温度和湿度，but不方便
# print(result[0])
# print(result[1])
#
# # 如果希望单独的处理元组的多个值，可以使用多个变量，一次接收函数的返回结果
# # 注意：使用的变量的个数应该和元组的元素个数保持一致
# gl_temp, gl_wetness = measure()
# print(gl_temp)
# print(gl_wetness)


# 经典面试题
"""
    题目要求
    1、有两个整数变量a=6，b=100
    2、不使用其他变量，交换两个值
"""
# 解法一 —— 使用其他变量
a = 6
b = 100

# c = a
# a = b
# b = c
#
# print(a)
# print(b)

# 解法二 —— 不使用其他变量
# a = a + b
# b = a - b
# a = a - b

# 解法三 —— python特有元组解法
# a, b = b, a
# # print(a)
# # print(b)


# (3) 函数的参数 进阶
# 1、只要针对参数使用赋值语句，会在函数内部修改局部变量的引用，不会影响到外部变量的引用

# def demo(num, num_list):
#
#     print("函数内部的代码")
#
#     # 在函数内部。针对参数使用赋值语句，不会修改到外部的实参变量
#     num = 100
#     num_list = [1, 2, 3]
#     print(num_list)
#     print(num)
#     print("函数执行完成")
#
#
# gl_num = 99
# gl_list = [4, 5, 6]
# demo(gl_num, gl_list)
# print(gl_num)
# print(gl_list)


# 2、如果传递的参数是可变类型，在函数内部，使用方法修改了数据的内容，同样会影响到外部的数据
# def demo(num_list):
#
#     print("函数内部的代码")
#
#     # 使用方法修改列表内容，其实它们指向的是同一个数据
#     num_list.append(9)
#     print(num_list)
#     print(id(num_list))  # 其实它们指向的是同一个数据
#     print("over")
#
#
# gl_list = [1,2,3,4]
# demo(gl_list)
# print(gl_list)
# print(id(gl_list))


# 3、 += （面试题）
# 列表变量调用 += 本质上是在执行列表变量的 extend方法，不会修改变量的引用,就会影响外部数据
# def demo(num, num_list):
#
#     print("start")
#
#     # num = num + num
#     num += num
#
#     # 列表变量使用 += 不会做相加在赋值的操作 ！
#     # num_list = num_list + num_list
#     # 本质上在调用 extend方法
#     num_list += num_list
#     # num_list.extend(num_list)
#
#     print(num)
#     print(num_list)
#
#     print("over")
#
# gl_num = 9
# gl_list = [1,2,3]
# demo(gl_num, gl_list)
# print(gl_num)
# print(gl_list)


# 4、缺省参数
"""
    定义函数时，可以给某个参数指定一个默认值，具有默认值的参数就叫做缺省参数
    调用函数时，如果没有传入缺省函数的是值，则在函数内部使用指定的默认参数值
    函数的缺省参数，将常见的值设置为参数的缺省值，从而简化函数的调用
"""
# 例如1 —— 对列表的排序方法
# gl_num_list = [13,6,3,11]
#
# gl_num_list.sort()
# print(gl_num_list)
#
# # sort方法的reverse就是一个缺省参数，实现降序排序
# gl_num_list.sort(reverse=True)
# print(gl_num_list)


# 缺省参数的注意事项
"""
    1、（定义的位置）必须保证带有默认值的缺省参数在参数列表的末尾
    2、（调用多个缺省参数） 如果有多个缺省参数，需要指定参数名，这样解释器才知道参数的对应关系
"""


# 指定函数的缺省参数
# 可以指定两个缺省参数，但必须保证带有默认值的缺省参数在参数列表的末尾
# def demo(name, title="", gender=True):
# def demo(name, title, gender=True):
#     """
#
#     :param title: 班上人的职位
#     :param name: 班上人的姓名
#     :param gender: True 表示男生， False 表示女生
#     """
#     gender_text = "男生"
#     if not gender:
#         gender_text = "女生"
#
#     print("[{}] {} 是{}".format(title, name, gender_text))
#
#
# # 提示： 在指定缺省参数时，需要使用最常见的作为默认值
# # 如果一个参数的值不能确定，则不应该设置默认值，具体的数值在调用函数时，有由外界传入！
# demo("Allen", "班长")
# demo("Jake", "学生")
# # 如果有多个缺省参数，需要指定参数名，这样解释器才知道参数的对应关系
# demo("Alan", "小组长", gender=False)


# 5、多值参数
"""
    需求 —— 可能需要处理的参数个数不确定，这个时候就可以使用多值参数
    python的两种多值参数：
    1、参数名前增加一个 * 可以接收元组
    2、参数名前增加两个 * 可以接收字典
    给多值参数的命名：
    3、 *args —— 存放元组参数，前面一个 *
    4、 ** kwargs —— 存放字典，前面两个 *
"""
# def demo(num, *args, **kwargs):
#
#     print(num)
#     print(args)
#     print(kwargs)
#
#
# demo(1,2,3,4, name="Allen", age=19)


# 多值参数案例 —— 计算任意多个数字的和
"""
    定义一个函数sum_numbers，可以计算任意个整数
    功能要求：将传递的值进行累加
"""
# def sum_numbers(*args):
# #
# #     num = 0
# #
# #     for n in args:
# #         num += n
# #     return num
# #
# #
# # result = sum_numbers(1,2,3,4,5)
# # print(result)


# 元组和字典的拆包
"""
    在调用带有多值参数的函数时，如果希望：
        将一个元组变量，直接传递给args
        将一个字典变量，直接传递给kwargs
    就可以使用拆包，简化参数的传递，
        在元祖变量前增加一个 *
        在字典变量前增加两个 *
"""

# def demo(*args, **kwargs):
#
#     print(args)
#     print(kwargs)
#
#
# # 元组变量/ 字典变量
# gl_tuple = (1,2,3,4)
# gl_dict = {"name": "Allen", "age": 19}
#
# # 错误方式
# # demo(gl_tuple, gl_dict)
#
# # 使用拆包语法,简化参数的传递
# demo(*gl_tuple, **gl_dict)
#
# # 基本方法
# demo(1,2,3, name="Allen", age=19)


# 6、函数的递归 —— 函数调用自身的编程技巧称为递归
"""
    代码特点：
    1、函数内部的代码是相同的，只是针对参数不同，处理的结果不同
    2、当参数满足一个条件时，函数不再执行，递归的出口，否则会死循环
"""
#
# def demo(num):
#
#     print(num)
#
#     # 递归的出口很重要，否则会死循环
#     if num == 1:
#         return
#
#     # 函数自己调用自己
#     demo(num - 1)
#
# demo(5)


# 定义一个函数，能过接收一个num的整数参数，计算1+2···+num的结果
# 递归是一个编程技巧，在处理不确定的循环条件时，格外的有用，列如：遍历整个文件目录一的结构
def sum_numbers(num):

    # 出口
    if num == 1:
        return 1

    # 2.数字的累加 num + (1 ··· num - 1)
    # 假设：sum_numbers能够正确处理1··num-1

    # temp = sum_numbers(num - 1)
    # return num + temp

    return num + sum_numbers(num - 1)


print(sum_numbers(100))