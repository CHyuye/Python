"""
    作者：陈志安
    功能：判断密码强弱

"""


class PasswordTool:

    def __init__(self, password):
        # 类的属性
        self.password = password
        self.strength_level = 0

    def process_pwd(self):
        # 规则一：长度大于8位数
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('您当前输入的密码少于8位数，请重新输入，谢谢！')

        # 规则二：包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('请输入带数字的密码！')

        # 规则三：包含字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('请输入带字母的密码！')

    # 定义函数方法
    def check_number_exist(self):
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True

        return has_number

    def check_letter_exist(self):
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True

        return has_letter


class FileTool:
    """
        文件工具类
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    """
        主函数
    """
    try_time = 5
    filepath = './password_6.0.txt'
    # 实例化文件工具类
    file_tool = FileTool(filepath)
    while try_time > 0:

        password = input('请输入您的密码:')

        # 创建密码工具对象
        password_tool = PasswordTool(password)
        password_tool.process_pwd()

        line = '密码：{}, 强度:{}\n'.format(password, password_tool.strength_level)

        # 写操作
        file_tool.write_to_file(line)

        # 判断密码是否合格
        if password_tool.strength_level == 3:
            print('恭喜，密码设置成功！')
            break
        else:
            print('密码等级过低，请重新输入，谢谢！')
            try_time -= 1

        print('-------------------------------')
    if try_time <= 0:
        print('亲，你尝试的次数过多，请稍等尝试！')

    # 读操作
    lines = file_tool.read_from_file()
    print(lines)


if __name__ == '__main__':
    main()
