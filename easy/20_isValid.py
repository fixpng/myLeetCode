# 20. 有效的括号
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # 括号的映射关系
        mapping = {')': '(', '}': '{', ']': '['}
        print(mapping)
        # 遍历字符串中的每个字符
        for char in s:
            # 如果是右括号
            if char in mapping:
                print(char)
                # 弹出栈顶元素，如果栈为空则赋值为 '#'
                top_element = stack.pop() if stack else '#'
                # 检查栈顶元素是否与当前右括号匹配
                if mapping[char] != top_element:
                    return False
            else:
                # 如果是左括号，则入栈
                stack.append(char)
        # 如果栈为空，则所有括号都匹配，返回 True，否则返回 False
        return not stack
    
# 测试用例
s = "()[]{}"
print(Solution().isValid(s))  # 输出：True
s = "(]"
print(Solution().isValid(s))  # 输出：False
        