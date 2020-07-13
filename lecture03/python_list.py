name_list = ['chen寒', 'zhen勤', 'fan程', 'sun悟空', 'zhu八戒', 'wu悟空']
num_list = [5, 10, 3, 13, 9]

# 1.取值和取索引
# 列表索引超出范围，程序报错
# print(name_list[0])
#
# # 知道数据内容，想确定数据在列表中的位置
# # index方法，传递的数据不在列表中，程序报错
# print(name_list.index('陈勤'))
#
# # 2.修改
# name_list[0] = 'chenhan'
# # 注意：指定索引超出范围，程序报错！
#
# # 3.增加
# # append方法，可以向列表的末尾追加数据
# name_list.append('王小二')
#
# # insert方法，可以在列表指定索引位置插入数据
# name_list.insert(1, "小美眉")
#
# # extend方法，可以把其他列表中的完整内容，追加到当前列表
# temp_list = ['孙悟空', '猪八戒', '沙师弟']
# name_list.extend(temp_list)
#
# # 删除
# # remove方法，可以从列表删除指定数据
# name_list.remove('chenhan')
#
# # pop 方法，默认可以把列表最后一个元素删除
# name_list.pop()
# # pop 方法，也可以指定要删除的元素索引
# name_list.pop(3)
#
# # del方法，关键字(delete)删除列表元素
# # 提示： 在日常开发时，要从列表删除数据，建议使用列表提供方法
# # del关键字会将变量从内存中删除，后续代码就不能再使用这个变量
# del name_list[1]
#
# # clear 方法，可以清空整个列表
# # name_list.clear()
#
# print(name_list)


# len(length 长度) 函数可以统计列表中元素的长度
# list_len = len(name_list)
# print("列表中有 %d 个元素" % list_len)
#
# # count方法，可以统计列表中某个数据出现的次数
# count = name_list.count('孙悟空')
# print("孙悟空在列表中出现了 %d 次" % count)
#
# # 从列表中删除第一次出现的数据，如果数据不存在，程序报错
# name_list.remove('孙悟空')


# 升序
# name_list.sort()  # 按英文字母排序
# num_list.sort()  # 大小

# 降序
# name_list.sort(reverse=True)
# num_list.sort(reverse=True)

# 逆序
# name_list.reverse()
# num_list.reverse()
#
# print(name_list)
# print(num_list)


# 迭代遍历列表

for my_name in name_list:
    """
        顺序的从列表中以此获取数据，每个循环过程中，数据都会保存在my_name
        这个变量中，在循环体内部可以访问到当前这一次获取到的数据
    """
    print('我的名字叫%s' % my_name)


