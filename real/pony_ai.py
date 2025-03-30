# 从某个字符串，需要经过多少步才能变成，target列表中的字符串的形式，中途不能出现forbidden列表的字符串

from collections import deque

def min_steps_to_target(start, target, forbidden):
    """
    计算从 start 字符串到 target 列表中任意一个字符串的最小步数，中途不能经过 forbidden 列表中的字符串。

    :param start: 初始字符串
    :param target: 目标字符串列表
    :param forbidden: 禁止出现的字符串列表
    :return: 最小步数，如果无法到达目标，返回 -1
    """
    # 使用队列进行广度优先搜索（BFS）
    queue = deque([(start, 0)])  # 队列存储 (当前字符串, 当前步数)
    visited = set([start])  # 记录已访问的字符串，避免重复访问
    forbidden_set = set(forbidden)  # 将 forbidden 转为集合，加速查找
    target_set = set(target)  # 将 target 转为集合，加速查找

    # 开始 BFS 搜索
    while queue:
        current, steps = queue.popleft()  # 从队列中取出当前字符串和步数

        # 如果当前字符串在目标集合中，返回步数
        if current in target_set:
            return steps

        # 遍历当前字符串的每个字符，尝试生成所有可能的下一步字符串
        for i in range(len(current)):
            for c in 'abcdefghijklmnopqrstuvwxyz':  # 假设只允许小写字母变化
                if c != current[i]:  # 确保字符发生变化
                    next_str = current[:i] + c + current[i+1:]  # 替换字符生成新字符串

                    # 如果新字符串未访问过，且不在 forbidden 集合中
                    if next_str not in visited and next_str not in forbidden_set:
                        visited.add(next_str)  # 标记为已访问
                        queue.append((next_str, steps + 1))  # 加入队列，步数加 1

    # 如果队列为空，仍未找到目标字符串，返回 -1
    return -1

# 示例调用
if __name__ == "__main__":
    # 起始字符串
    start = "abc"
    # 目标字符串列表
    target = ["ayc"]
    # 禁止出现的字符串列表
    forbidden = ["bbc", "xbc"]
    # 输出从 start 到 target 中任意一个字符串的最小步数
    print(min_steps_to_target(start, target, forbidden))  # 示例输出
