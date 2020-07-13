""""
    作者：陈志安
    功能：计算BRM
"""


def main():
    """
    主函数

    """

    y_or_n = input('是否退出程序(y/n)')

    while y_or_n != 'y':
        # # 性别
        # gender = input('性别：')
        # # print(type(gender)) type()可以用来查看字符串的类型
        # # 体重
        # weight = float(input('体重(Kg)：'))
        # # 身高(cm)
        # height = float(input('身高(CM):'))
        # # 年龄
        # age = float(input('年龄：'))

        # 字符串分割 str.split()
        print('请输入以下信息，用空格进行分隔')
        input_str = input('性别 体重(Kg) 身高(CM) 年龄(岁): ')
        str_list = input_str.split(' ')

        try:
            gender = str_list[0]
            weight = float(str_list[1])
            height = float(str_list[2])
            age = int(str_list[3])

            if gender == '男':
                # 男生
                bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66

            elif gender == '女':
                # 女生
                bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 65

            else:
                bmr = -1

            if bmr != -1:
                # 字符串格式化输出，使用{}占位 .format 语句 注意是.format()
                print('您的性别：{}，体重：{}公斤，身高：{}厘米，年龄：{}岁'.format(gender, weight, height, age))
                print('您的基础代谢率为：{}(卡路里)'.format(bmr))

            else:
                print('系统暂不支持该操作，谢谢！')

        except ValueError:
            print('请输入正确的信息！')
        except IndexError:
            print('请输入完整的信息！')
        except:
            print('程序异常操作！')

        print()  # 输出空行
        y_or_n = input('是否退出程序(y/n)?')

    if y_or_n == 'y':
            print('程序已退出')


if __name__ == '__main__':
    main()