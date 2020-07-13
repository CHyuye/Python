"""
    深度优先搜索 -- 目的也是从起点开始搜索直到指定顶点
    深度优先搜索会沿着一条路径不断往下搜索直到不能继续为止，然后再折返，开始搜索下一条后补路径

"""

from collections import deque


# 首先定义一个创建的类，使用邻接矩阵
class Graph(object):
    def __init__(self, *args, **kwargs):
        self.order = []
        self.neighbor = {}

    def add_node(self, node):
        key, val = node
        if not isinstance(val, list):
            print("节点输入时应该为一个线性表")  #
        self.neighbor[key] = val

    def DFS(self, root):
        # 首先判断节点是否为空节点
        if root != None:
            search_queue = deque()
            search_queue.append(root)

            visited = []

        else:
            print('root is None')
            return -1

        while search_queue:
            person = search_queue.popleft()
            self.order.append(person)

            if (not person in visited) and (person in self.neighbor.keys()):
                tmp = self.neighbor[person]
                tmp.reverse()

                for index in tmp:
                    search_queue.appendleft(index)

                visited.append(person)

    def clear(self):
        self.order = []

    def node_print(self):
        for index in self.order:
            print(index, end='  ')


if __name__ == '__main__':
    # 创建一个二叉树图
    g = Graph()
    g.add_node(('A', ['B', 'C']))
    g.add_node(('B', ['D', 'E']))
    g.add_node(('C', ['F']))

    # 进行深度优先搜索
    print('深度优先搜索：')
    print('  ', end='  ')
    g.DFS('A')
    g.node_print()
    print()