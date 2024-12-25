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
        min_price = prices[0] # we take min_price to the first index value of prices list 

        for price in prices[1:]:
            min_price = min(min_price, price) # we take the minimum value of min_price and price 
            max_profit = max(max_profit, price - min_price) # we take the maximum value of max_profit and price - min_price 

        return max_profit
    



#NOTE:prices = [7, 1, 5, 3, 6, 4]
# max_profit = 0
# min_price = 7  # Initialize min_price to the first element of prices

# Iteration 1:
# Price is 1, which is smaller than min_price (7).
# Update min_price to 1.
# Calculate profit: 1 - 7 = -6 (negative, so we don't update max_profit).
# max_profit remains 0.

# Iteration 2:
# Price is 5, which is greater than min_price (1).
# Update max_profit to max(0, 5 - 1) = 4.
# max_profit becomes 4.

# Iteration 3:
# Price is 3, which is smaller than min_price (1).
# Update min_price to 3.
# Calculate profit: 3 - 1 = 2.
# Update max_profit to max(4, 2) = 4 (max_profit remains 4).

# Iteration 4:
# Price is 6, which is greater than min_price (3).
# Update max_profit to max(4, 6 - 3) = 4 (max_profit remains 4).

# Iteration 5:
# Price is 4, which is smaller than min_price (3).
# Update min_price to 4.
# Calculate profit: 4 - 3 = 1.
# Update max_profit to max(4, 1) = 4 (max_profit remains 4).

# End of loop

# The final value of max_profit is 4, which represents the maximum profit achievable by buying the stock at price 1 and selling it at price 6.

# print("Maximum Profit:", max_profit)


# Example usage:
# if __name__ == "__main__":
#     prices = [7, 1, 5, 3, 6, 4]
#     result = maxProfit(prices)
#     print("Maximum Profit:", result)

# @lc code=end

