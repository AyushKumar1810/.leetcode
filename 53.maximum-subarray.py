#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums):
        maxsub=nums[0]
        currsum=0
        for n in nums :
            if currsum < 0 :
                currsum=0
            currsum+=n
            maxsub=max(maxsub , currsum)
        return maxsub


        
# @lc code=end

