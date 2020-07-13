"""
    作者：陈志安
    日期：19/3/21
    功能：AQI计算
    版本：v.7
    网络爬虫
"""
import requests
from bs4 import BeautifulSoup
import csv


def get_city_aqi(city_pinyin):
    """
        获取城市的aqi
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()

        # 第一种方式 city_aqi.append((caption, value))
        city_aqi.append(value)
    return city_aqi


def get_all_cities():
    """
        获取所有的城市
    """
    url = 'http://pm25.in/'
    city_list = []
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')

    city_div = soup.find_all('div', {'class': 'bottom'})[1]
    city_link_list = city_div.find_all('a')
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name, city_pinyin))
    return city_list


def main():
    """
        主函数
    """
    city_list = get_all_cities()
    header = ['city', 'AQI', 'PM2.5/h', 'PM10/h', 'CO/h', 'NO2/h', 'O3/h', 'O3/8h']

    with open('china_city_aqi.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i, city in enumerate(city_list):
            if (i + 1) % 10 == 0:
                print('已处理{}条记录，（共{}条记录）'.format(i + 1, len(city_list)))

            city_name = city[0]
            city_pinyin = city[1]
            city_aqi = get_city_aqi(city_pinyin)
            row = [city_name] + city_aqi
            writer.writerow(row)


if __name__ == '__main__':
    main()
