#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
#Note: pls note the difference between this problem and knapsack
# 1. In Knapsack, there is no compulsion that each number should be included to achieve a sum
# 2. In Knapsack, there are positive numbers. Hence, for this problem : in the base case (target = 0 and empty/non-empty set), we cant blindly initialise it to 1.
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
# @lc code=end

