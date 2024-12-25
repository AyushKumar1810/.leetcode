#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums) 

#     # Calculate the sum of numbers from 0 to n using the arithmetic formula (n*(n+1))/2
#         expected_sum = (n * (n + 1)) // 2

#     # Calculate the actual sum of the elements in the array
#         actual_sum = sum(nums)

#     # The missing number is the difference between the expected sum and the actual sum
#         return expected_sum - actual_sum
#     # def missingNumber(nums):
#         # # missing = len(nums)
#         # # for i, num in enumerate(nums):
#         # #     missing ^= i ^ num
        # # return missing

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
        
        
# @lc code=end

