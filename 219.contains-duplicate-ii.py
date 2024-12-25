#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {} # key: num, value: index of num in nums list 
        for i, val in enumerate(nums): # i is the index of val in nums list 
            if val in seen and i - seen[val] <= k: # if the value is in seen and the difference between the current index and the index of the value in seen is less than or equal to k, return True 
                return True 
            else:
                seen[val] = i
        return False


        
# @lc code=end

