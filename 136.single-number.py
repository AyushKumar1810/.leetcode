#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums):
        res=0
        for n in nums:
            res=n^res
        return res
        
# @lc code=end

