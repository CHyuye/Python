"""
    广度优先搜索 -- 一种对图进行搜索的算法
    广度优先搜索会优先从离起点近的顶点开始搜索

"""

from collections import deque  # 模块提供一些有用的集合类
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def research(name):
    research_queue = deque()  # 建立一个双端队列
    research_queue += graph[name]  # 将你的邻居都加入到这个搜索队列中
    searched = []  # 这个数组用来记录已检查过的人
    while research_queue:  # 队列不为空时循环执行
        person = research_queue.popleft()  # 对队列中的第一项进行判断，出队
        if person not in searched:  # 仅当这个人没检查时才检查
            if person_is_seller(person):  # 如果是person就打印
                print(person + " is a mango seller.")
            else:  # 如果person不是商人，就将person的朋友都加入搜索队列
                research_queue += graph[person]
                searched.append(person)  # 讲这个人标记为检查过


def person_is_seller(name):  # 名字最后一个为‘m’就是商人
    return name[-1] == 'm'


research('you')

