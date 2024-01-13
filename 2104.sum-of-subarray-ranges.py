#
# @lc app=leetcode id=2104 lang=python3
#
# [2104] Sum of Subarray Ranges
#

# @lc code=start
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0

        for i in range(n):
            min_val = float('inf')
            max_val = float('-inf')

            for j in range(i, n):
            # Update min_val and max_val as we extend the subarray
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])

            # Calculate the contribution of the current subarray
                total_sum += (max_val - min_val)

        return total_sum



        
# @lc code=end

