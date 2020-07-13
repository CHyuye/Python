"""
    狄克斯特拉算法 —— 求解最短路径问题，该算法多了一步选择顶点的操作，因此求最短路径更为高效
    狄克斯特拉算法在有负权重时不能使用，它会找到一个错误的最短路径。
    在不存在负权重时，更适合用狄克斯特拉算法，而存在负权重时，即便更为耗时，也应该使用正确答案的
    贝尔曼-福特算法

"""

# 数据关系模型用字典嵌套字典的形式来表达
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'D': 1, 'E': 3},
    'C': {'B': 6, 'F': 8},
    'D': {'E': 4},
    'E': {'G': 9},
    'F': {'G': 7},
    'G': {}
}

# 定义耗时字典
costs = {}
costs['A'] = 0

# 存储父节点的字典
parents = {}


def find_lowest_cost_node(node, node_cost):
    """找到A下一级的节点，并更新costs里的值，和parents里面的值"""
    # 获取当前的节点所有下一级节点的权重
    for next_node in graph[node].keys():
        # 判断next_node是否存在costs里
        if next_node in costs.keys():
            if graph[node][next_node] + node_cost < costs[next_node]:
                costs[next_node] = graph[node][next_node] + node_cost
                parents[next_node] = node
            else:
                continue
        else:
            costs[next_node] = graph[node][next_node] + node_cost
            parents[next_node] = node


def find_path(node):
    """利用递归算法，获取parents里面的父节点"""
    super_node = parents[node]
    print(super_node)
    if super_node is not "A":
        super_node = find_path(super_node)
        return super_node
    else:
        return 'A'


def main():
    """主函数部分"""
    node = 'A'

    while node is not 'G':
        # 找到costs中最小值的键，将其从costs里面剔除
        node = min(costs, key=costs.get)
        node_cost = costs[node]
        del costs[node]
        if graph[node]:
            find_lowest_cost_node(node, node_cost)
        else:
            # 如果没有下一级节点，就继续找一个最小的节点
            continue

    # parents里面打印出来的，就可以从终点开始追溯到父节点，最终到起点
    print(parents)

    # 获取父节点，并打印出来
    finally_node = 'G'
    print(finally_node)
    find_path(finally_node)


if __name__ == '__main__':
    main()

