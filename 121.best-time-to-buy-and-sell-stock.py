#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0

        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

# Example usage:
# if __name__ == "__main__":
#     prices = [7, 1, 5, 3, 6, 4]
#     result = maxProfit(prices)
#     print("Maximum Profit:", result)

# @lc code=end

