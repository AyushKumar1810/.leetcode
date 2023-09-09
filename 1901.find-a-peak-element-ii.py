    #
# @lc app=leetcode id=1901 lang=python3
#
# [1901] Find a Peak Element II
#

# @lc code=start
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                is_peak = True

                if i > 0 and mat[i - 1][j] > mat[i][j]:
                    is_peak = False
                if i + 1 < m and mat[i + 1][j] > mat[i][j]:
                    is_peak = False
                if j > 0 and mat[i][j - 1] > mat[i][j]:
                    is_peak = False
                if j + 1 < n and mat[i][j + 1] > mat[i][j]:
                    is_peak = False

                if is_peak:
                    return [i, j]

        return []

       

        
# @lc code=end

