#
# @lc app=leetcode id=1283 lang=python3
#
# [1283] Find the Smallest Divisor Given a Threshold
#

# @lc code=start
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def division_sum(divisor):
            return sum((num + divisor - 1)//divisor for num in nums)
        left , right=1 , max(nums)
        while left < right:
            mid = (left + right)//2
            if division_sum(mid) <=threshold:
                right = mid
            else:
                left = mid+1

        return left
# @lc code=end

