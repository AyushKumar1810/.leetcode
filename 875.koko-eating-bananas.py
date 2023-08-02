#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        Sum=sum(piles)

        l=ceil(Sum/h)
        r=ceil(Sum/(h-len(piles)+1))

        while l<r:
            m=(l+r)//2
            t=0
            for pile in piles:
                t+=ceil(pile/m)
            if t>h:
                l=m+1
            else:
                r=m
        
        return l
        
# @lc code=end

