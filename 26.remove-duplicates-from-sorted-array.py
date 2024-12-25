#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List

class Solution:
    def removeDuplicates(self,nums: List[int]) -> int:
        left = 0  # Initialize the left pointer to the 0th index
        for right in range(1, len(nums)):  # The right pointer goes from the 1st index to the last
            if nums[left] != nums[right]:  # If left is not equal to right, increment the left pointer
                left += 1
                nums[left] = nums[right]  # Assign the right value to the left and continue the loop

        return left + 1 


    # @lc code=end

