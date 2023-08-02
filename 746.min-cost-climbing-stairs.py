#
#@lc app=leetcode id=746 lang=python3
#
#[746] Min Cost Climbing Stairs
#

#@lc code=start
class Solution:
    def minCostClimbingStairs(self, cost):
        cost.append(0)
        for i in range (len(cost)-3,-1,-1):# We are iletrating from 
            # right to left with 2nd last digit 
            cost[i]=cost[i] + min(cost[i+1] , cost[i+2])
        return min(cost[0], cost[1])

        
# @lc code=end

