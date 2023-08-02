#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums):
        hashSet=set() #1 Will not give repeated numbers       
        for num in nums:        
            if num in hashSet: #2
                return True             
            hashSet.add(num)
        return False    
        
# @lc code=end

