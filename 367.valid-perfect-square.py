#
# @lc app=leetcode id=367 lang=python
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l,r=1,num
        while l <=r:
            mid=(l+r)//2
            if mid * mid > num:
                r=mid-1
            elif mid * mid < num :
                l=mid + 1
            else :
                 return True
        return False
    
# @lc code=end

