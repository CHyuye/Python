"""
    作者：陈志安
    日期：19/3/21
    功能：AQI计算
    版本：v.5
    网络爬虫
"""
import requests


def get_html_text(url):
    """
        返回url的文本
    """
    r = requests.get(url, timeout=30)
    # print(r.status_code)
    return r.text


def main():
    """
        主函数
    """
    city_pinyi = input('请输入城市拼音：')
    url = 'http://pm25.in/' + city_pinyi
    url_text = get_html_text(url)

    aqi_div = ''' <div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_val = url_text[begin_index: end_index]
    print('空气质量为{}'.format(aqi_val))


if __name__ == '__main__':
    main()
