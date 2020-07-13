"""
    定义函数 -- 封装独立的功能
    调用函数 -- 享受封装的成果
"""
# 练习一
# import program_03  # 导入
#
# program_03.multiple_table()  # 函数的调用


# 注意：函数定义好之后，只表示这个函数封装了一段代码
# 如果不调用函数，函数是不会主动执行的
# 注意：不能把函数调用放在函数的上方

# 练习二
# name = "小明"
#
# print(name)
#
#
# def say_hello():
#
#     print("Hello word!")
#     print("Hello word!")
#     # print(name)
#
#
# say_hello()
#
# print(name)


# 练习三
# 函数参数的使用
# def sun_two_num(num1, num2):  # 形参 —— 定义函数，用来接收参数用的，在函数内部作为变量使用
# #     """对两个数字的求和"""
# #     result = num1 + num2
# #
# #     print("%d + %d = %d" % (num1, num2, result))
# #
# #
# # sun_two_num(50, 20)  # 实参 —— 调用函数，用来把数据传递到函数内部

# 练习四
# 函数返回值 —— 返回值是函数完成工作后，最后给调用者的一个结果
# 在函数中使用return可以返回结果 注意：return表示返回，后续的代码都不会被执行
#
# def sum_2_num(num1, num2):
#
#     # 使用返回值，告诉调用函数一方计算的结果
#     return num1 + num2
#
# # 可以使用变量，来接收函数执行的返回结果
# result = sum_2_num(10, 30)
# print("计算结果：%d" % result)


# # 练习五
# # 函数嵌套调用的执行路线
# def test1():
#
#     print("*" * 50)
#
#
# def test2():
#
#     test1()
#     print("-" * 50)
#
# test2()


# 练习六
# 函数嵌套演练 —— 打印分隔线

# 需求一：打印一条分隔线
# def print_line():
#
#     print("*" * 50)

# print_line()

# 需求二 —— 打印一条由任意字符,可以重复次数组成的分割线

# def print_line(char, times):
#     """
#         打印一条分隔线
#     :param char: 分割字符
#     :param times: 重复次数
#     """
#     print(char * times)
#
#
# print_line("#", 30)


# 需求三 —— 打印多条分割线
#
# def print_line(char, times):
#
#     print(char * times)
#
#
# def print_lines(char, times):
#     """
#         打印多行分割线
#     :param char: 分隔线使用的分隔字符
#     :param times: 分隔符重复次数
#     """
#     row = 0
#     while row < 5:
#
#         print_line(char, times)
#
#         row += 1

#
# print_lines("!", 40)


# import program_03
#
# # 模块名.变量 / 模块名.函数
# program_03.print_line("#", 30)
# print(program_03.name)