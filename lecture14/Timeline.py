from pyecharts import Bar, Timeline
from random import randint

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
bar_1 = Bar("2015年销量", "数据纯属虚构")
bar_1.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_1.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_1.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_1.add("冬季", attr, [randint(10, 100) for _ in range(6)])

bar_2 = Bar("2016年销量", "数据纯属虚构")
bar_2.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_2.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_2.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_2.add("冬季", attr, [randint(10, 100) for _ in range(6)])

bar_3 = Bar("2017年销量", "数据纯属虚构")
bar_3.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_3.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_3.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_3.add("冬季", attr, [randint(10, 100) for _ in range(6)])

bar_4 = Bar("2018年销量", "数据纯属虚构")
bar_4.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_4.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_4.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_4.add("冬季", attr, [randint(10, 100) for _ in range(6)])

bar_5 = Bar("2019年销量", "数据纯属虚构")
bar_5.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_5.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_5.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_5.add("冬季", attr, [randint(10, 100) for _ in range(6)], is_legend_show=True)

timeline = Timeline(is_auto_play=True,
                    timeline_bottom=0,
                    timeline_play_interval=800
                    )
timeline.add(bar_1, '2015年')
timeline.add(bar_2, '2016年')
timeline.add(bar_3, '2017年')
timeline.add(bar_4, '2018年')
timeline.add(bar_5, '2019年')
