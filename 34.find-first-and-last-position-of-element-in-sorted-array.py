#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def binary(self,nums,target,leftbias):
        left,right=0,len(nums)-1
        i=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                i=mid
                if leftbias:
                    right=mid-1
                else:
                    left=mid+1
        return i
    def searchRange(self, nums , target ):
        left=self.binary(nums,target,True)
        right=self.binary(nums,target,False)
        return [left,right]
        
# @lc code=end

