# 深度优先搜索 DFS
# 深度优先搜索是一种用于遍历或搜索树或图的算法。

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