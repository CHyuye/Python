"""
    作者：陈志安
    功能：计算出时间，是几年几天
"""

from datetime import datetime


def is_leap_year(year):
    """
        判断是否是闰年
    """
    is_leap = False

    if (year % 400 == 0) or (year % 4 == 0) and (year != 0):
        is_leap = True

    return is_leap


def main():
    """
        主函数
    """
    input_date_str = input('请输入日期(yyyy/mm/dd):')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day
    # 键值对 字典
    # month_day_dict = {1: 31,
    #                   2: 28,
    #                   3: 31,
    #                   4: 30,
    #                   5: 31,
    #                   6: 30,
    #                   7: 31,
    #                   8: 31,
    #                   9: 30,
    #                   10: 31,
    #                   11: 30,
    #                   12: 31}

    day_month_dict = {30: {4, 6, 9, 11},
                      31: {1, 3, 5, 7, 8, 10, 12},
                      28: {2}}

    days = 0
    days += day

    for i in range(1, month):
        if i in day_month_dict[30]:
            days += 30
        elif i in day_month_dict[31]:
            days += 31
        else:
            days += 28

    if is_leap_year(year) and month > 2:
        days += 1

    print('这是{}年的第{}月的第{}天'.format(year, month, days))


if __name__ == '__main__':
    main()