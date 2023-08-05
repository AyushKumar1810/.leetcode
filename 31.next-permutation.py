#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start

# from typing import List
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) # size of the array.

    # Step 1: Find the break point:
        ind = -1 # break point
        for i in range(n-2, -1, -1): # we will go reverse
            if nums[i] < nums[i + 1]:
            # index i is the break point
                ind = i
                break

    # If break point does not exist:
        if ind == -1:
        # reverse the whole array:
            nums.reverse()
            return nums

    # Step 2: Find the next greater element
        #         and swap it with arr[ind]:
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

    # Step 3: reverse the right half:
        nums[ind+1:] = reversed(nums[ind+1:])

        return nums
# @lc code=end

