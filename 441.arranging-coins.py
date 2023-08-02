#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
#Actually 1 + 2 + 3 + 4 ... n = n (n + 1) / 2 is a serie where 
#n is equal to the last term of our serie and also represents
# the number of terms so all we need is just solve the equation n = i*(i + 1)/2
        
        start, end = 0, n
        while start <= end:
            mid = (start+end)//2
            guess = mid*(mid+1)//2
            if guess > n:
                end = mid-1
            elif guess <= n:
                start = mid+1
                row = mid
        return row
        # return int(((0.25 + 2 * n) ** 0.5) - 1/2)
        
# @lc code=end

