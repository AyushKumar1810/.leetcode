#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums ):
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for r in range(len(nums)):
            if nums[r]: # if not 0
                nums[l] , nums[r] = nums[r] , nums [l] # we are swapping 
                # left value with right value
                l=l+1# then we are increament out left pointer
        return nums
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero  = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1
        return nums


# @lc code=end

