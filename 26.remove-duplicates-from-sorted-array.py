#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums):
        l=1 #initiallt left pointer =1
        for r in range(1 , len(nums)):# Right Pointers From 1 To nums 
#Here we are comapring 1st index nums value with 0Th index nums value 
            if nums[r] != nums[r-1]:
                nums[l]=nums[r]#if it's not eaual then update into nums[l] 
                l=l+1
        return l
        
# @lc code=end

