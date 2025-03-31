# 100. 相同的树
"""
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

# Example usage:
if __name__ == "__main__":
    # Create two identical trees
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    print(p.val, q.val)  # Output: 1 1
    print(p.left.val, q.left.val)  # Output: 2 2
    print(p.right.val, q.right.val)  # Output: 3 3
    
    
    solution = Solution()
    print(solution.isSameTree(p, q))  # Output: True

    # Create two different trees
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))

    print(solution.isSameTree(p, q))  # Output: False
    # Create two identical trees with different structures
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, None, TreeNode(3))
    print(solution.isSameTree(p, q))  # Output: False
