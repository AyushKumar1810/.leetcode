#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)  # Size of the array

    # Edge cases:
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2

        # If arr[mid] is the peak:
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid

        # If we are in the left:
            if nums[mid] > nums[mid - 1]:
                low = mid + 1

        # If we are in the right:
        # Or, arr[mid] is a common point:
            else:
                high = mid - 1

    # Dummy return statement
        return -1
        
# @lc code=end

