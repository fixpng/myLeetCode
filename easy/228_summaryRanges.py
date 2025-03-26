# 228. 汇总区间
"""
给定一个  无重复元素 的 有序 整数数组 nums 。
返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。
列表中的每个区间范围 [a,b] 应该按如下格式输出：
"a->b" ，如果 a != b
"a" ，如果 a == b
"""


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        def f(i: int, j: int) -> str:
            return str(nums[i]) if i == j else f'{nums[i]}->{nums[j]}'

        i = 0
        n = len(nums)
        ans = []
        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            ans.append(f(i, j))
            i = j + 1
        return ans

# class Solution:
#     def summaryRanges(self, nums: list[int]) -> list[str]:
#         if not nums:  # 如果数组为空，直接返回空列表
#             return []
        
#         result = []  # 存储结果的列表
#         start = nums[0]  # 初始化区间的起始数字
        
#         for i in range(1, len(nums)):
#             # 如果当前数字与前一个数字不连续
#             if nums[i] != nums[i - 1] + 1:
#                 # 判断区间是单个数字还是范围
#                 if start == nums[i - 1]:
#                     result.append(str(start))  # 单个数字
#                 else:
#                     result.append(f"{start}->{nums[i - 1]}")  # 范围
#                 start = nums[i]  # 更新起始数字为当前数字
        
#         # 处理最后一个区间
#         if start == nums[-1]:
#             result.append(str(start))
#         else:
#             result.append(f"{start}->{nums[-1]}")
        
#         return result


# 测试用例
nums = [0, 1, 2, 4, 5, 7]
print(Solution().summaryRanges(nums))  # 输出：["0->2", "4->5", "7"]