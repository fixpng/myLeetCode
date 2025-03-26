# 205. 同构字符串
"""
给定两个字符串 s 和 t ，判断它们是否是同构的。
如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
        

s = "egg"
t = "add"
print(len(set(s)))  # 输出：2
print(len(set(t)))  # 输出：2
print(len(set(zip(s, t))))  # 输出：2

print(Solution().isIsomorphic(s, t))  # True

s = "foo"
t = "bar"
print(len(set(s)))  # 输出：2
print(len(set(t)))  # 输出：3
print(len(set(zip(s, t))))  # 输出：3
print(Solution().isIsomorphic(s, t))  # False


s = "paper"
t = "title"
print(Solution().isIsomorphic(s, t))  # True