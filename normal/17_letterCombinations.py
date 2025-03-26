# 17. 电话号码的字母组合
"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def backtrack(index, path):
            if index == len(digits):
                res.append(''.join(path))
                return
            for i in phone[digits[index]]:
                path.append(i)
                backtrack(index + 1, path)
                path.pop()
        res = []
        backtrack(0, [])
        return res

digits = "23"
print(Solution().letterCombinations(digits)) 


digits = "2352"
print(Solution().letterCombinations(digits)) 