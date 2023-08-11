#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums):
        left =0  # basically we are taking one pointer to 0th index 
        for right in range (1,len(nums)): # for second pointer it will go from 1st index to last
            if nums[left] != nums[right]: # If left is not equal to right then we will increase left pointeer to 1 
                left = left +1
                nums[left] = nums [right] # and we will assign right value to the left and loop continue till last 

        return left +1 
    # @lc code=end

