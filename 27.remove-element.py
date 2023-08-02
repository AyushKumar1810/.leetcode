#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums,val):
        for v in nums[:]:
            if v==val:
                nums.remove(v)
        return len(nums)
        
# @lc code=end

