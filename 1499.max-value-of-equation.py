#
# @lc app=leetcode id=1499 lang=python3
#
# [1499] Max Value of Equation
#

# @lc code=start
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        res = -inf
        i = 0
        n = len(points)
        last = 0

        while i < n:
            if i >= last:
                last = i + 1

            for j in range(last, n):
                if points[j][0] > k + points[i][0]: #Here we have checked This  
                    # "j - i <= k. " conditions 
                    break
                else:
                    tp = points[i][1] + points[j][1] + points[j][0] - points[i][0] # here that y[i] + y[j] + |x[i] - x[j]| conditions 
                    if tp > res:
                        res = tp
                        last = j
            i += 1
        return res


        
# @lc code=end

