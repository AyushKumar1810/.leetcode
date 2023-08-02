#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, n):
        if n<=0:
            return False
        for p in [2,3,5]:
            while n%p==0:
                n=n//p
        return n==1
                    
        
# @lc code=end

