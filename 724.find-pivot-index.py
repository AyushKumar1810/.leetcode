#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums):
        total =sum(nums)
        leftsum=0
        for i in range(len(nums)):
            rightsum=total - nums[i] - leftsum # for getting right sum 
            # we have to subtract it from total sum with the current left sum and
            # current index value at which we are 
            if leftsum ==rightsum : # if right sum == left sum then 
                # return that index value 
                return i 
            leftsum = leftsum + nums[i]
        return -1
        
# @lc code=end

