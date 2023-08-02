#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Create a dynamic programming array to store the minimum path sums
        dp = [0] * (len(triangle) + 1)
        
        # Iterate through the triangle from bottom to top
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                # Update the current element in the dp array with the minimum path sum
                dp[i] = n + min(dp[i], dp[i+1])
        
        # Return the minimum path sum at the top of the triangle
        return dp[0]


        
# @lc code=end

