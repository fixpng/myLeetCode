# 121. 买卖股票的最佳时机
"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
 

提示：

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        # 1. 初始化最小价格为第一个元素，最大利润为0
        min_price = prices[0]
        max_profit = 0
        
        # 2. 遍历列表，计算每个元素与最小价格之间的差值，并更新最大利润
        for price in prices:
            profit = price - min_price
            max_profit = max(profit, max_profit)
            min_price = min(price, min_price)
        
        # 3. 返回最大利润
        return max_profit
    
# 示例调用
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print(solution.maxProfit(prices))  # 输出: 5
    
    prices = [7, 6, 4, 3, 1]
    print(solution.maxProfit(prices))  # 输出: 0
