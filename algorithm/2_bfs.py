# 广度优先搜索算法(Breadth First Search) BFS
# 适用于无权图的最短路径问题
# 适用于最小步数问题，如求解最短路径、最短距离、最短时间等
# 适用于搜索问题，如迷宫、图形遍历等

from collections import deque
from typing import List, Tuple, Set
import string

def bfs(start: str, target: List[str], forbidden: List[str]) -> int:
    """
    使用广度优先搜索算法计算从 start 字符串到 target 列表中任意一个字符串的最小步数，中途不能经过 forbidden 列表中的字符串。
    
    :param start: 初始字符串
    :param target: 目标字符串列表
    :param forbidden: 禁止出现的字符串列表
    :return: 最小步数，如果无法到达目标，返回 -1
    """
    if not start or not target or not forbidden:
        return -1
    q = deque()  # 队列用于存储待处理的字符串和当前步数
    visited = set()  # 集合用于存储已访问的字符串，避免重复访问
    forbidden_set = set(forbidden)  # 将 forbidden 转为集合，加速查找
    target_set = set(target)  # 将 target 转为集合，加速查找
    q.append((start, 0))  # 将初始字符串和步数 0 加入队列
    visited.add(start)  # 将初始字符串标记为已访问
    while q:
        current, steps = q.popleft()
        # 如果当前字符串在目标集合中，返回步数
        if current in target_set:
            return steps
        for i in range(len(current)):  # 遍历当前字符串的每个字符
            for c in string.ascii_lowercase:
                if c != current[i]:  # 确保字符发生变化
                    next_str = current[:i] + c + current[i+1:]  # 替换字符生成新字符串
                    # 如果新字符串未访问过，且不在 forbidden 集合中
                    if next_str not in visited and next_str not in forbidden_set:
                        visited.add(next_str)  # 标记为已访问
                        q.append((next_str, steps + 1))  # 加入队列，步数加 1
                        if next_str in target_set:
                            return steps + 1  # 如果新字符串在目标集合中，直接返回步数
    return -1  # 如果队列为空，仍未找到目标字符串，返回 -1

if __name__ == '__main__':
    start = "hit"
    target = ["hot", "dot", "dog", "lot", "log", "cog"]
    forbidden = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(bfs(start, target, forbidden))
    # 示例输出: 4
    # 解释: 从 "hit" -> "hot" -> "dot" -> "dog" -> "cog" 需要 4 步
    # 但由于 "hot" 在 forbidden 列表中，所以返回 -1
    # 解释: 无法到达目标字符串，返回 -1