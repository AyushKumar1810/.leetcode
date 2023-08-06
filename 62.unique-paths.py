#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N=n+m-2
        r=m-1
        res=1
        for i in range(1,r+1):
            res=res*(N-r+i)/i
        return int(res)

        
# @lc code=end

