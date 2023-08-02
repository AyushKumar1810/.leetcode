#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        left = 0 
        min_length=float('inf')
        current_sum=0
        for right in range(n):
            current_sum =current_sum + nums[right]
            while current_sum >=target:
                min_length=min(min_length, right - left +1)
                current_sum -=nums[left]
                left +=1
        return int(min_length )if min_length !=float('inf') else 0

        
# @lc code=end

