#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
# class NumArray:
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.dp = [0] * (len(nums) + 1)
#         for i in range(len(nums)):
#             self.dp[i + 1] = self.dp[i] + nums[i]
#     def sumRange(self, left: int, right: int) -> int:
#         return self.dp[right + 1] - self.dp[left]
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums 
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

