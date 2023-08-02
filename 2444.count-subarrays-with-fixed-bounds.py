#
# @lc app=leetcode id=2444 lang=python3
#
# [2444] Count Subarrays With Fixed Bounds
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        count = 0
        left = 0
        result = 0

        for right in range(n):
            if self.mink <= self.arr[right] <= self.R:
                # If the current element is within the bounds, we update the result
                # by adding the count of valid subarrays ending at the current element.
                count = right - left + 1
                result += count
            elif self.arr[right] < self.L:
                # If the current element is less than L, there are no valid subarrays
                # ending at the current element, so we update the left pointer.
                left = right + 1
            else:  # self.arr[right] > self.R
                # If the current element is greater than R, it can break the continuity
                # of the subarrays, so we reset the count and the left pointer.
                count = 0
                left = right + 1

        return result

# Example
# arr = [1, 3, 5, 2, 7, 5]
# L = 1
# R = 5
# print(count_subarrays_with_bounds(arr, L, R))  # Output: 2

        
# @lc code=end

