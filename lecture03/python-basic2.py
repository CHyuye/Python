
# 练习一
# 定义一个变量
# age = int(input("请输入你的年龄："))
#
# if age >= 0 and age <= 120:
#     print("你的年龄正确！")
# else:
#     print("你的年龄不正确")
#
# # 练习二
# python_score = int(input("请输入您的python语言成绩："))
# c_score = int(input("请输入您的C语言成绩："))
#
# if python_score > 60 or c_score > 60:
#     print("恭喜您成绩合格！")
# else:
#     print("考试不及格，继续努力！")
#
# # 练习三
# # 在开发中，通常希望某个条件不满足时，执行一些代码，可以使用not
# # 另外，如果需要拼接复杂的逻辑计算条件，同样使用not
# is_employee = False
#
# if not is_employee:
#     print("非本公司人员，禁止入内！")
# else:
#     print("OK!")

# # 练习四——女朋友的的节日
# # holiday_name = str(input("请输入您当前的节日："))
# #
# # if holiday_name == "情人节":
# #     print("买玫瑰花")
# #     print("看电影")
# # elif holiday_name == "平安夜":
# #     print("买苹果")
# #     print("吃大餐")
# # elif holiday_name == "生日":
# #     print("过生日，吃蛋糕")
# # else:
# #     print("生活的每天都是节日啊...")

# 练习五———火车站安检
# 定义是否有车票
has_ticket = str(input("请出示您的火车票(是/否)?"))

if has_ticket == "是":
    # 定义道具长度
    print("车票检查通过，准备开始安检！")
    knife_length = int(input("请配合检查您携带刀具的长度(厘米)？"))
    if knife_length <= 20:
        print("审核已通过，祝您旅途愉快！")
    else:
        print("您携带的管制刀具有 %d 厘米，不允许上车！" % knife_length)
else:
    print("您还未买火车，请前往售票处购买！")


