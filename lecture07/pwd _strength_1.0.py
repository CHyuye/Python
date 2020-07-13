"""
    作者：陈志安
    功能：判断密码强弱

"""

# def check_number_exist(password_str):
#     """
#         判断是否含有数字
#     """
#     for c in password_str:
#         if c.isnumeric():
#             return True
#     return False
#
#
# def check_letter_exist(password_str):
#     """
#         判断是否含有字母
#     """
#     for c in password_str:
#         if c.isalpha():
#             return True
#     return False
#
#
# def main():
#     """
#         主函数
#     """
#     password = input('请输入密码：')
#
#     # 密码强度
#     strength_level = 0
#
#     # 规则一：密码长度大于8
#     if len(password) >= 8:
#         strength_level += 1
#     else:
#         print('请输入大于8位的密码！')
#
#     # 规则二：密码包含数字
#     if check_number_exist(password):
#         strength_level += 1
#     else:
#         print('请输入带数字的密码！')
#
#     # 规则三：密码包含字母
#     if check_letter_exist(password):
#         strength_level += 1
#     else:
#         print('请输入带字母的密码！')
#
#     if strength_level == 3:
#         print('密码设置成功！')
#     else:
#         print('密码等级过低，请重新输入！')
#
#
# if __name__ == '__main__':
#     main()

import turtle


def draw_branch(branch_length):

    if branch_length > 5:
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - 15)

        turtle.left(40)
        draw_branch(branch_length - 15)

        turtle.right(20)
        turtle.backward(branch_length)


def main():

    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.color('red')
    draw_branch(100)
    turtle.exitonclick()


if __name__ == '__main__':
    main()

turtle.done()

# turtle.pensize(2)
# turtle.bgcolor("black")
# colors = ["red", "yellow", "purple", "blue"]
# turtle.tracer(False)
# for x in range(400):
#     turtle.forward(2*x)
#     turtle.color(colors[x % 4])
#     turtle.left(91)
# turtle.tracer(True)





