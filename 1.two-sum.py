#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums) - 1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#More optimized solution 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], i]
            num_dict[num] = i
        return None
#example usage 
# print(s.twoSum([2, 7, 11, 15], 9))

        
# @lc code=end

