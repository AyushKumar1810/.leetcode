#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:    
        mapST,mapTS={},{}
        for i in range (len(s)):
            c1,c2=s[i],t[i]
            if ((c1 in mapST and mapST[c1] !=c2)or
                (c2 in mapTS and mapTS[c2] !=c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True        
# @lc code=end

