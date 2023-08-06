#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: # if power is 0
            return 1

        if n < 0: # if power is negative then x will be reciprocal and we will make n positive(as we already have converted x to 1/x)
            x = 1 / x
            n = -n

        result = 1
        while n: # If x > 0
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result

        
# @lc code=end

