#
# @lc app=leetcode id=795 lang=python3
#
# [795] Number of Subarrays with Bounded Maximum
#

# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        result = 0
        start , end =-1 , -1
        for i in range(len(nums)):
            if nums[i] > right:
                start = i
            if nums[i] >=left:
                end = i
            result+=end -start
        return result
                
# @lc code=end

