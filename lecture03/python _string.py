"""
    字符串 —— 一串字符，是编程语言中表示文本的数据类型
    大多数编程语言都是使用 ""  来定义字符串
"""
# # r如果字符串外部需使用 ',可以使用 “ 定义字符串
# str1 = "Hello Python"
# # 如果字符串内部需要使用 ", 可以使用 ‘ 定义字符串
# str2 = '我的外号是"大西瓜"'
#
# print(str1)
# print(str2)
#
# for char in str1:
#
#     print(char)


# str_ABC = "Hello Python hello"
# # 1.统计字符串长度
# print(len(str_ABC))
#
# # 2.统计某个子字符串出现的次数
# print(str_ABC.count("ll"))
# print(str_ABC.count("ABC"))
#
# # 3.某个字符串出现的位置
# print(str_ABC.index("P"))
# 如果使用index方法，查找的字符串不存在，程序报错！
# print(str_ABC.index("A"))


"""
    1）判断类型 - 9
    string.isspace() -- 如果string只包含空格，则返回True
    string.isalnum() -- 如果string有一个字符并且所有字符都是字母或者数字，返回True
    string.isalpha() -- 如果string有一个字符或者都是字母，返回True
    string.isdecimal() -- 如果string只包含数字，则返回True，[全角数字]
    string.isdigit() -- 如果string只包含数字，则返回True，[全角数字、(1)、\u00b2]
    string.isnumeric() -- 如果string只包含数字，[全角数字、汉字数字]
    string.istitle() -- 如果string是标题化(每个首字母大写)则返回True
    string.islower() -- 如果string有小写字母或者都是小写字母，则返回True
    string.isupper() -- 如果string有大写字母或者都是大写字母，则返回True
"""

# str_space = "    \t\n\r"
#
# print(str_space.isspace())
#
# alnum_str = "123abc"
#
# print(alnum_str.isalnum())
#
# pha_str = "abc"
#
# print(pha_str.isalpha())
#
# # isdecimal和isdigit、isnumeric方法作比较
# # 1> 都不能判断小数
# # num_str = "1.1"
# # 2> Unicode 字符串
# # num_str = "\u00b2"
# # 3> 中文数字
# num_str = "一千零一"
#
# print(num_str)
# print(num_str.isdecimal())  # isdecimal方法不能判断字符串
# print(num_str.isdigit())
# print(num_str.isnumeric())  # 能判断中文数字

# istitle和islower、isupper方法作比较
# Eng_str = "abc"
# Eng_str = "ABCD"
#
# print(Eng_str.istitle())  # 只有当首字母是大写时为True
# print(Eng_str.islower())  # 只有小写字母为True
# print(Eng_str.isupper())  # 只有当字符串都是大写时为True


"""
    2）查找和替换 - 7
    string.startswith(str) —— 检查字符串是否以str开头，是则返回True
    string.endswith(str) —— 检查字符串是否以str结尾，是则返回True
    string.find(str, start=0, end=len(string)) —— 检查str是否在string中，如果start和end范围内，是则返回索引，不是则返回-1
    string.rfind(str, start=0, end=len(string)) —— 类似find方法，不过是从右边开始查找
    string.index(str, start=0, end=len(string)) —— 跟find方法类似，如果str不存在会报错
    string.rindex(str, start=0, end=len(string)) —— 跟index方法类似，不过从右边查找
    string.replace(old_str, new_str, num=string.count(old)) —— 把string中的old_str替换成new_str,如果num指定，则替换不超过num次

"""

# demo_str = "Hello Python is a very good"
#
# # 1.判断是否以指定字符串开始
# print(demo_str.startswith("hello"))
#
# # 2.判断是否以指定字符串结束
# print(demo_str.endswith("good"))
#
# # 3.查找指定字符串
# print(demo_str.find("is"))
# # index()方法，如果指定字符串不存在，会报错
# # find()方法，如果指定字符串不存在，返回-1
# print(demo_str.find("an"))
#
# # 4.替换字符串
# # replace方法执行完成后，会返回一个新的字符串
# # 注意：不会修改原有字符串内容
# print(demo_str.replace("Python", "World"))
#
# print(demo_str)



"""
    3）字符串大小写转换 —— 5
    string.capitalize() —— 把字符串的第一个字符大写
    string.title() —— 把字符串每个单词首字母大写
    string.lower() —— 转换字符串每个都小写
    string.upper() —— 转换字符串每个都大写
    string.swapcase() —— 翻转字符串的大小写
"""

demo_str = "i LovE allen"
#
print(demo_str.capitalize())
#
# print(demo_str.title())
#
# print(demo_str.lower())
#
# print(demo_str.upper())
#
# print(demo_str.swapcase())
# print(demo_str)


"""
    4）文本对齐 —— 3
    string.ljust(width) —— 返回一个原字符串左对齐，并使用空格填充至长度width的新字符串
    string.rjust(width) —— 返回一个原字符串右对齐，并使用空格填充至长度width的新字符串
    string.center(width) —— 返回一个原字符串居中，并使用空格填充至长度width的新字符串
"""
#
# poem_str = ["\t登鹳雀楼\n",
#             "王之涣\n",
#             "白日依山尽，  ",
#             "黄河入海流。",
#             "欲穷千里目，",
#             "更上一层楼。\t"
#             ]

# for poem in poem_str:
#     # print("|%s|" % poem.center(10, "　"))  # fillchar需要传递一个全角空格
#     print("|%s|" % poem.ljust(10, "　"))

"""
    5）去除空白字符 —— 3
    string.lstrip() —— 截掉string左边(开始)的空白字符
    string.rstrip() —— 截掉string右边(末尾)的空白字符
    string.strip() —— 截掉string左右两边的空白字符
    
"""

# for poem in poem_str:
#     # 先使用strip方法去除空白字符
#     # 在使用center方法居中显示文本
#     print("|%s|" % poem.strip().center(10, "　"))

"""
    拆分和连接 —— 5
    string.partition(str) —— 把字符串分成一个3元素的元组(str前面，str后面)
    string.rpartition(str) ——— 类似partition()方法，不过是从右边开始查找
    string.split(str="", num) —— 以str为分隔符切片string，如果num有指定值，则仅分隔num+1个字符串，str默认包含\r,\t,\n和空格
    string.splitlines() —— 按照行(\r',\n', '\r\n')分隔，返回一个包含各行作为元素的列表
    string.join(seq) —— 以string为分隔符，将seq中所有的元素(的字符串表示)合并为一个新的字符串
"""
#
# poem_str = "登鹳雀楼\t 王之涣\n\t 白日依山尽\t 黄河入海流\n 欲穷千里目\t 更上一层楼"
#
# print(poem_str)
# # 要求：1.将字符串中的空白字符去除  2.在使用" " 作为分隔符，拼接成整齐的字符串

# # 1.拆分字符串
# poem_list = poem_str.split()
# print(poem_list)
#
# # 2.合并字符串
# poem_result = " ".join(poem_list)
# print(poem_result)


# 字符串切片
"""
    切片方法适用于字符串、列表、元组
    切片使用索引值来限定范围，从大的字符串切出小的字符串
"""
# 字符串切片格式  字符串[开始索引:结束索引:步长]

num_str = "0123456789"

# 1.截取2-5位置字符串
print(num_str[2:6])

# 2.截取2-末尾
print(num_str[2:])

# 3.截取从开始到6
print(num_str[:7])

# 4.截取完整字符串
print(num_str[::])

# 5.从开始每隔一个截取  获取到的是偶数
print(num_str[::2])

# 6.从1开始每隔一个截取 获取到的是奇数
print(num_str[1::2])

# 7.截取从2-末尾-1的字符串
print(num_str[2:-1])

# 8.截取字符串末尾两个字符串
print(num_str[-2:])

# 9.字符串逆序(面试题)
print(num_str[::-1])
print(num_str[-1::-1])