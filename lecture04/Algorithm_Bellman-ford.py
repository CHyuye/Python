"""
    贝尔曼-福特算法 —— 一种在图中求解最短路问题的算法。最短路径问题就是在就是在加权图
    指定了起点和终点的前提下，寻找从起点到终点的路径中权重总和最小的那条路径

"""

def Bellman_ford(graph, source):
    dist = {}
    p = {}
    max = 10000
    for v in graph:
        dist[v] = max  # 赋值为负无穷完成初始化
        p[v] = None
    dist[source] = 0

    for i in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if dist[v] > graph[u][v] + dist[u]:
                    dist[v] = graph[u][v] + dist[u]
                    p[v] = u   # 完成松弛操作，p为前驱节点

    for u in graph:
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                return None, None  # 判断是否存在环路

    return dist, p


def test():
    graph = {
        'a': {'b': -1, 'c': 4},
        'b': {'c': 2, 'd': 3, 'e': 2},
        'c': {},
        'd': {'b': 3, 'c': 5},
        'e': {'d': -3}
    }
    dist, p = Bellman_ford(graph, 'a')
    print(dist)
    print(p)


def testfail():
    graph = {
        'a': {'b': -1, 'c': 4},
        'b': {'c': 2, 'd': 3, 'e': 2},
        'c': {'d': -5},
        'd': {'b': 3},
        'e': {'d': -3}
    }
    dist, p = Bellman_ford(graph, 'a')
    print(dist)
    print(p)


test()
testfail()
