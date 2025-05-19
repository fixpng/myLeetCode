# 530. 二叉搜索树的最小绝对差
"""
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

差值是一个正数，其数值等于两值之差的绝对值。
输入：root = [4,2,6,1,3]
输出：1

输入：root = [1,0,48,null,null,12,49]
输出：1

树中节点的数目范围是 [2, 104]
0 <= Node.val <= 105
"""

from typing import Optional
import math  # 补充 math 模块以定义 inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = math.inf  # 使用 math.inf 表示正无穷
        pre = -math.inf  # 使用 -math.inf 表示负无穷

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs(node.left)
            nonlocal ans, pre
            ans = min(ans, node.val - pre)
            pre = node.val
            dfs(node.right)

        dfs(root)
        return ans
    

# 示例调用
if __name__ == "__main__":
    # 创建二叉搜索树
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    # 创建 Solution 对象
    solution = Solution()

    # 调用 getMinimumDifference 方法
    result = solution.getMinimumDifference(root)
    print(result)  # 输出: 1
