#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start


#NOTE:Approach
# The array either contains all positive elements (so from 1 to len(nums)), or it is missing one of those numbers. In the first case, we can return len(nums) + 1. In the second case, we can use cycle sort and try to move the ones that do exist to the "right" position.

# We use cycle sort to move any element from 1 to len(nums) to index - 1 positon. Then, we can go through the array and see which element is not equal to its index + 1.
class Solution:
    def firstMissingPositive(self , nums):
        n = len(nums)

    # Rearrange the array to place each positive integer at its correct index
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # Find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

    # If all integers are in their correct positions, return the next positive integer
        return n + 1

# Example usage:
# nums = [3, 4, -1, 1]
# result = firstMissingPositive(nums)
# print(result)        
        
# @lc code=end

