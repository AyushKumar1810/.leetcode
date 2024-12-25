#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
# class Solution:
#     def removeElement(self, nums,val):
#         for v in nums[:]:
#             if v==val:
#                 nums.remove(v)
#         return len(nums)
class Solution:
    def removeElement(self, nums, val):
        while val in nums: # while val is in nums list 
            nums.remove(val) # remove the first occurrence of val in nums list 
        return len(nums) # return the length of nums list after removing all val in nums list 


# @lc code=end

