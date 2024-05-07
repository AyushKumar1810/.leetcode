#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#


# @lc code=start

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to keep track of maximum profit
        buy1 = buy2 = float('-inf')  # Initially set to negative infinity to ensure proper updates
        sell1 = sell2 = 0  # Initially set to 0, as no profit is earned yet
        
        # Iterate through each price in the prices array
        for price in prices:
            # Update buy1: maximum profit after the first buy
            buy1 = max(buy1, -price)  # Take the maximum between current buy1 and the negative of the price
            
            # Update sell1: maximum profit after the first sell
            sell1 = max(sell1, buy1 + price)  # Take the maximum between current sell1 and buy1 + price
            
            # Update buy2: maximum profit after the second buy
            buy2 = max(buy2, sell1 - price)  # Take the maximum between current buy2 and sell1 - price
            
            # Update sell2: maximum profit after the second sell
            sell2 = max(sell2, buy2 + price)  # Take the maximum between current sell2 and buy2 + price
        
        # Return the maximum profit achieved after completing two transactions
        return sell2

        
# @lc code=end

