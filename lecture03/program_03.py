""""
    作者：陈志安
    功能：分形树
    版本：1.0

"""

import turtle


def draw_tree(length):
    if length > 5:
        turtle.forward(length)
        turtle.right(20)
        draw_tree(length - 10)

        turtle.left(40)
        draw_tree(length - 10)

        turtle.right(20)
        turtle.backward(length)


def main():
    turtle.speed(9)
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    draw_tree(80)
    turtle.done()


if __name__ == '__main__':
    main()


def multiple_table():  # 函数的封装
    """九九乘法表"""
    for i in range(1, 10):
        for j in range(1, i+1):
            print('%d × %d= %d' % (j, i, i*j), end='\t')
        print()


def print_line(char, times):

    print(char * times)


def print_lines(char, times):
    """
        打印多行分割线
    :param char: 分隔线使用的分隔字符
    :param times: 分隔符重复次数
    """
    row = 0
    while row < 5:

        print_line(char, times)

        row += 1


# print_lines("-", 10)

# name = "黑马程序员"
