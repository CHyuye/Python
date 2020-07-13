# 公共方法

"""
    Python内置函数
    len() —— 计算容器中元素个数
    del() —— 删除元素
    max() —— 返回最大值，如果是字典只针对key
    min() —— 返回最小值，如果是字典只针对key
    cmp() —— 比较两个值，python3.x已取消
"""
demo_list = [1, 5, 8, 10, 6]
demo_str = "ahuienkciawiehiz"
demo_tuple = (5, 9, 0, 8, 1)
demo_dict = {"a": "z", "b": "y", "c": "w"}
# del demo_list[1]
# del(demo_list[0])
# print(demo_list)

# print(max(demo_list))
# print(min(demo_str))
# print(max(demo_dict))

# 切片 —— 支持的数据类型：字符串，列表，元组
# print(demo_tuple[1:3])

# 运算符
# + 合并 支持的数据类型：字符串，列表，元组
# * 重复 支持的数据类型：字符串，列表，元组

# 成员运算符 —— 对字典操作时，判断的是字典键(key)
# "in" 元素是否存在  支持的数据类型：字符串，列表，元组，字典
# "not in" 元素是否不存在 支持的数据类型：字符串，列表，元组，字典

# 完整的for循环演练
# for num in demo_list:
#
#     print(num, end="  ")
#
#     if num == 8:
#         break
#
# else:
#     # 如果循环体内部使用break退出循环
#     # else 下方的代码就不会被执行
#     print("会被执行吗？")
#
# print("循环结束！")

# 应用场景
# students = [
#     {"name": "陈寒"},
#     {"name": "谢雨"}
# ]
#
# find_name = "谢雨"
#
# for stud_dict in students:
#
#     print(stud_dict)
#
#     if stud_dict["name"] == find_name:
#
#         print("找到了 %s" % find_name)
#         break
# else:
#     print("抱歉没有找到 %s" % find_name)

# print("循环结束！")

print([3] in [1,2,3,4])
print(abs(-3))
print(int('101', 2))
print(int('123', 8))
print(max('11','1','3','9'))
print(min('9','5','3','18'))