# 79. 单词搜索
"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
"""

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, index):
            # 如果所有字符都匹配，返回 True
            if index == len(word):
                return True
            # 检查边界条件和当前字符是否匹配
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            # 临时保存当前字符并标记为已访问
            temp, board[r][c] = board[r][c], '#'
            # 在四个方向上继续搜索
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            # 恢复当前单元格的值
            board[r][c] = temp
            return found
        
        # 遍历网格中的每个单元格作为起点
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


# 示例用法
if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    print(Solution().exist(board, word))  # 输出: False

    word = "ABCCED"
    print(Solution().exist(board, word))  # 输出: True

