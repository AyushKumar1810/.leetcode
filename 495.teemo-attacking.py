#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total_time = 0
        for i in range(1, len(timeSeries)):
            total_time += min(timeSeries[i] - timeSeries[i-1], duration) # min() is used to handle the case when the duration is greater than the difference between the two timeSeries elements  
        return total_time + duration 
        
# @lc code=end

