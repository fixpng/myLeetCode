# 102. 二叉树的层序遍历 (Medium)
"""
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # 初始化二叉树节点，包含值、左子节点和右子节点
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 如果树为空，直接返回空列表
        if not root: return []
        
        result = []  # 用于存储最终的层序遍历结果
        queue = [root]  # 使用队列存储当前层的节点，从根节点开始
        
        while queue:
            level_size = len(queue)  # 当前层的节点数量
            level_nodes = []  # 当前层的节点值列表
            
            for _ in range(level_size):
                # 从队列中取出一个节点
                node = queue.pop(0)
                print(f"当前节点值: {node.val}")  # 打印当前节点值
                level_nodes.append(node.val)  # 将节点值加入当前层的结果
                
                # 如果左子节点存在，加入队列
                if node.left: queue.append(node.left)
                # 如果右子节点存在，加入队列
                if node.right: queue.append(node.right)
            
            # 将当前层的节点值列表加入最终结果
            result.append(level_nodes)
            print(f"当前层的节点值: {level_nodes}")  # 打印当前层的节点值
        
        return result  # 返回层序遍历结果
    

if __name__ == "__main__":
    # 构造示例二叉树
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    solution = Solution()
    # 调用层序遍历方法并打印结果
    result = solution.levelOrder(root)
    print(result)  # Output: [[3], [9, 20], [15, 7]]
