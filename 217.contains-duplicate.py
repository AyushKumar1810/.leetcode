#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums):
        hashSet=set() #1 Will not give repeated numbers in set        
        for num in nums:        
            if num in hashSet: #2 If number is already in set, then return True 
                return True             
            hashSet.add(num) #3 If number is not in set, then add it to set
        return False     #4 If no number is repeated, then return False 
    
 

# @lc code=end

