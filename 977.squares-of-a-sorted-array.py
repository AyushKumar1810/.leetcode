#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums):
        res=[]
        l,r=0,len(nums) - 1
        while l <=r:
            if nums[l]*nums[l] > nums[r]*nums[r]:
                res.append(nums[l]*nums[l])
                l=l+1
            else:
                res.append(nums[r]*nums[r]) 
                r=r-1
        return res[::-1] # reversing it 
# @lc code=end

