"""
    作者：陈志安
    日期：19/3/21
    功能：AQI计算
    版本：v.1
"""

import json
import csv
import os


def process_json_file(filepath):
    """
        解码json文件
    """
    # f = open(filepath, mode='r', encoding='utf-8')
    # city_list = json.load(f)
    # return city_list
    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)


def process_csv_file(filepath):
    """
        处理CSV文件
    """
    with open(filepath, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row))


def main():
    """
        主函数
    """
    filepath = input('请输入文件名称：')
    filename, file_ext = os.path.splitext(filepath)
    if file_ext == '.json':
        # json文件
        process_json_file(filepath)
    elif file_ext == '.csv':
        # csv文件
        process_csv_file(filepath)
    else:
        print('您的输入有误！')


if __name__ == '__main__':
    main()
