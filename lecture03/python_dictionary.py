"""
    —— 字典 —— 通常用哪个来描述一个物体的相关信息，可以存储多个数据
    和列表的区别：列表是有序的对象集合 字典是无序的对象集合
    字典用{}定义
    字典使用键值对存储数据，键值对之间用','分割
    键和值用':'链接
    键必须是唯一的
    值可以取任何数据类型，但键只能使用字符串，数字，元组

"""

# 字典是无序的数据集合
character_dict = [{'name': 'Allen',
                   'age': 18,
                   'gender': 'Man',
                   'height': 170,
                   'weight': 55,
                   'hobby': 'write code'},
                  {'name': 'Clean',
                   'age': 20,
                   'gender': 'Women',
                   'height': 165,
                   'weight': 45,
                   'hobby': 'play music'}

                  ]

Allen_dict = {'name': 'Allen', 'age': 18, 'gender': 'Man', 'height': 170, 'weight': 55, 'hobby': 'write code'}


# # 1.取值
# print(Allen_dict['name'])
# # 在取值时，如果指定的key不存在，程序报错！
# # print(xiaoming_dict['name1'])
#
# # 2.增加/修改
# # 如果key不存在，会新增键值对
# Allen_dict['hobby'] = 'write code'
# # 如果key存在，会修改已经存在的键值对
# Allen_dict['age'] = 20
#
# # 3.删除
# Allen_dict.pop('weight')


# 1.统计键值对数量
# print(len(Allen_dict))
#
# # 2. 合并字典 -- update
# temp_dict = {'love color': 'Green', 'age': 19}
#
# # 注意：如果合并的字典中包含已经存在的键值对，会覆盖原有的键值对
# Allen_dict.update(temp_dict)
#
# # 3. 清空字典
# Allen_dict.clear()


# 字典的遍历
# 变量k是每一次循环中，获取到的键值对的key
# for k in Allen_dict:
#
#     print("%s -- %s" % (k, Allen_dict[k]))


# 字典的遍历实际应用场景不多
# 1.使用多个键值对，存储描述一个物体的相关信息  —— 描述更复杂的数据信息
# 2.将多个字典放在一个列表中，在进行遍历，再循环体内针对每个字典进行相同的处理
for character_info in character_dict:

    print(character_info)