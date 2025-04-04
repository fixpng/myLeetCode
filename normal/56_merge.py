# 56. 合并区间
"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
"""


from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # 按照区间的开始位置进行排序
        intervals.sort(key=lambda x: x[0])  # 使用 lambda 函数作为排序的键
        # 初始化合并后的区间列表
        merged = [intervals[0]]  # 初始化合并后的区间列表
        print(merged)

        for i in range(1, len(intervals)):
            current = intervals[i]
            print(current)
            last_merged = merged[-1]

            # 如果当前区间与最后一个合并的区间重叠，则进行合并
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                merged.append(current)

        return merged
        


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))  # 输出：[[1,6],[8,10],[15,18]]
print("end")
intervals = [[1,4],[4,5]]
print(Solution().merge(intervals))  # 输出：[[1,5]]
print("end")