# 从某个字符串，需要经过多少步才能变成，target列表中的字符串的形式，中途不能出现forbidden列表的字符串

from collections import deque
import time  # 添加时间模块
from typing import List, Tuple, Set


# bfs函数实现
# 广度优先搜索算法(Breadth First Search) BFS
def bfs(start: str, target: List[str], forbidden: List[str]) -> int:
    """
    使用 BFS 算法计算从 start 到 target 的最小步数，禁止经过 forbidden 中的字符串。
    
    :param start: 起始字符串
    :param target: 目标字符串列表
    :param forbidden: 禁止出现的字符串列表
    :return: 最小步数，如果无法到达目标，返回 -1
    """
    queue = deque([(start, 0)])  # 队列存储 (当前字符串, 当前步数)
    visited = set([start])  # 记录已访问的字符串，避免重复访问
    forbidden_set = set(forbidden)  # 将 forbidden 转为集合，加速查找
    target_set = set(target)  # 将 target 转为集合，加速查找
    print(queue)  # 调试输出，查看队列状态
    while queue:
        current, steps = queue.popleft()  # 从队列中取出当前字符串和步数
        print(f"当前字符串: {current}, 步数: {steps}")  # 调试输出，查看当前字符串和步数
        # 如果当前字符串在目标集合中，返回步数
        if current in target_set:
            print(f"找到目标字符串: {current}, 步数: {steps}")
            print("队列长度：",len(queue))
            return steps
        for i in range(len(current)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != current[i]:
                    next_str = current[:i] + c + current[i+1:]
                    # 如果新字符串未访问过，且不在 forbidden 集合中
                    if next_str not in visited and next_str not in forbidden_set:
                        print(f"尝试替换字符: {current[i]} -> {c}  new: {next_str}")  # 调试输出，查看替换的字符
                        visited.add(next_str)
                        queue.append((next_str, steps + 1))
    # 如果队列为空，仍未找到目标字符串，返回 -1
    return -1



# 示例调用
if __name__ == "__main__":
    # 起始字符串
    start = "aac"
    # 目标字符串列表
    target = ["asa", "cbc"]
    # 禁止出现的字符串列表
    forbidden = ["bbc", "xbc"]
    # 输出从 start 到 target 中任意一个字符串的最小步数
    

    start_time = time.time()  # 记录开始时间
    
    print(bfs(start, target, forbidden))  # 示例输出
    
    end_time = time.time()  # 记录结束时间
    print(f"耗时: {end_time - start_time:.10f} 秒")  # 输出耗时
