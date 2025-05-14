# 67. 二进制求和
"""
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。

示例 1：

输入:a = "11", b = "1"
输出："100"
示例 2：

输入：a = "1010", b = "1011"
输出："10101"
 

提示：

1 <= a.length, b.length <= 104
a 和 b 仅由字符 '0' 或 '1' 组成
字符串如果不是 "0" ，就不含前导零
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 1. 先将两个二进制字符串转换为十进制整数
        a = int(a, 2)
        b = int(b, 2)
        # 2. 将两个十进制整数相加
        c = a + b
        # 3. 将结果转换为二进制字符串并去掉前缀 '0b'
        return bin(c)[2:]

if __name__ == "__main__":
    # 测试用例
    a = "11"
    b = "1"
    print(Solution().addBinary(a, b))  # 输出: "100"

    a = "1010"
    b = "1011"
    print(Solution().addBinary(a, b))  # 输出: "10101"