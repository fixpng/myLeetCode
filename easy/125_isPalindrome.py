# 125. 验证回文串
"""
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
字母和数字都属于字母数字字符。
给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
"""

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         i, j = 0, len(s) - 1
#         while i < j:
#             if not s[i].isalnum():
#                 i += 1
#             elif not s[j].isalnum():
#                 j -= 1
#             elif s[i].lower() == s[j].lower():
#                 i += 1
#                 j -= 1
#             else:
#                 return False
#         return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]
        


s = "A man, a plan, a canal: Panama"
print(s)
print(s[3:])
print(list(filter(str.isalnum, s)))
print(s.isalnum())

print(Solution().isPalindrome(s)) # True

s = "race a car"
print(Solution().isPalindrome(s)) # False