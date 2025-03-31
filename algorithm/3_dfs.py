# 深度优先搜索 DFS depth-first search
# 深度优先搜索是一种用于遍历或搜索树或图的算法。
# 它从根节点开始，沿着树的深度遍历尽可能深的节点，然后回溯。
# 深度优先搜索可以用递归或栈实现。
# 在图中，深度优先搜索可以用于寻找路径、检测环、拓扑排序等。
# 深度优先搜索的时间复杂度为 O(V + E)，其中 V 是节点数，E 是边数。
# 空间复杂度为 O(V)，用于存储访问过的节点。
# 深度优先搜索的优点是实现简单，适用于较小的图或树。
# 缺点是可能会陷入死循环，特别是在图中存在环时。

def dfs(graph: dict, start: str, target: str, visited: set = None) -> bool:
    """
    深度优先搜索实现。
    :param graph: 图的邻接表表示
    :param start: 起始节点
    :param target: 目标节点
    :param visited: 已访问节点集合
    :return: 是否可以到达目标节点
    """
    if visited is None:
        visited = set()
    # 如果找到目标节点，返回 True
    if start == target:
        return True
    # 标记当前节点为已访问
    visited.add(start)
    # 遍历邻居节点
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True
    return False


if __name__ == '__main__':
    # 示例图的邻接表表示
    graph = {
        "hit": ["hot"],
        "hot": ["dot", "lot"],
        "dot": ["dog"],
        "dog": ["cog"],
        "lot": ["log"],
        "log": ["cog"],
        "cog": []
    }
    start = "hit"
    target = "cog"
    forbidden = {"hot"}  # 禁止访问的节点

    # 从图中移除禁止访问的节点及其边
    for node in forbidden:
        graph.pop(node, None)
        for neighbors in graph.values():
            if node in neighbors:
                neighbors.remove(node)

    # 测试 DFS
    visited = set()
    result = dfs(graph, start, target, visited)
    print(result)  # 示例输出: False
    # 解释: 由于 "hot" 被禁止访问，无法到达目标节点 "cog"