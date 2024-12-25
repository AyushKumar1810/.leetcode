#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() # sort the children 
        s.sort() # sort the cookies 
        i, j = 0, 0
        while i < len(g) and j < len(s): 
            if g[i] <= s[j]: # if the cookie is bigger than the child's greed factor, then the child is content 
                i += 1      # move to the next child 
            j += 1         # move to the next cookie 
        return i
        
# @lc code=end

