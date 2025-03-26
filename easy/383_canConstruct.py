# 383. 赎金信
"""
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。
"""

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         for char in set(ransomNote):  # 遍历 ransomNote 中的唯一字符
#             if ransomNote.count(char) > magazine.count(char):  # 检查字符数量是否足够
#                 return False
#         return True

# from collections import defaultdict

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         char_count = defaultdict(int)
#         # 统计 magazine 中每个字符的数量
#         for char in magazine:
#             char_count[char] += 1
#         # 检查 ransomNote 中的字符是否足够
#         for char in ransomNote:
#             if char_count[char] == 0:  # 如果字符不足
#                 return False
#             char_count[char] -= 1  # 使用一个字符
#         return True

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        print(f"ransomNote: {ransomNote}, magazine: {magazine}")  # 调试信息
        return Counter(ransomNote) <= Counter(magazine)


# Test cases
ransomNote = "a"
magazine = "b"
print(Solution().canConstruct(ransomNote, magazine))  # False

ransomNote = "aa"
magazine = "ab"
print(Solution().canConstruct(ransomNote, magazine))  # False

ransomNote = "aa"
magazine = "abab"
print(Counter(ransomNote))
print(Counter(magazine))
print(Solution().canConstruct(ransomNote, magazine))  # True