"""
    break -- 某一个条件满足时，退出循环，不再执行后续代码
    continue -- 某一个条件满足时，跳出循环体剩余部分，开始新一轮循环
"""
# # break -- 某一个条件满足时，退出循环，不再执行后续代码
# i = 0
#
# while i < 10:
#     if i == 3:
#         break
#
#     print(i)
#
#     i += 1
#
# print("over")
#
#
# # continue -- 某一个条件满足时，不执行后续重复代码，开始新一轮循环
# i = 0
#
# while i < 10:
#     if i == 4:
#         # 注意：在使用continue关键字之前，需要确认循环的技术是否修改，否则会导致死循环
#         i += 1
#         continue
#
#     print(i)
#
#     i += 1
# print("over")

# while 循环嵌套
# 练习一 嵌套打印小星星

# row = 1
#
# while row <= 5:
#
#     print("*" * row)
#
#     row += 1

# # 1> 完成5行内容的简单输出
# # 2> 分析每行内部的 * 如何处理？
# row = 1
#
# while row <= 5:
#
#     # 增加一个小循环，处理每列的 * 显示
#     # 定义列计数器
#     col = 1
#     # 开始循环
#     while col <= row:
#
#         # print("%d列" % col)
#         print("*", end="")
#
#         col += 1
#     # print("%d行" % row)
#     # 这行代码的目的是在一行星星输出完成后，添加换行
#     print("")
#
#     row += 1

# print函数扩展——print函数输出内容之后，会自动在内容末尾增加换行
# 如果不希望增加换行，在后面加end=""
#
# print("*", end="---")
# # 单纯换行
# print("*")


# 练习二 —— 循环打印九九乘法表
# 方法一
# row = 1
#
# while row <= 9:
#
#     col = 1
#     while col <= row:
#         print("%d × %d = %d" % (row, col, row * col), end="\t")
#         col += 1
#
#     print("")
#     row += 1

# 方法二
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d × %d = %d" % (j, i, j*i), end="\t")
#     print("")

"""
    \t -- 在控制台输出一个制表符，使输出文本垂直方向保持对齐
    \n -- 在输出台输出一个换行符
    \" -- 在输出台输出一个双引号
    \' -- 在输出台输出一个单引号
    \\ -- 在输出台输出一个反斜杠符号
    \t -- 回车
"""
# print("Can\" do python")
# print("I\'am China chen")
# print("Hello\\python")
