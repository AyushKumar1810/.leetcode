#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums, target):
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m] >target:
                r=m-1
            elif nums[m] < target:
                l=m+1
            else:
                return m 
        return -1
                

        
# @lc code=end

