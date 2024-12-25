#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums)) # remove duplicates and convert to list to sort it 
        if len(nums) < 3:
            return max(nums)
        nums.sort()
        return nums[-3] # return the third max number from the end of the list 

        
# @lc code=end

