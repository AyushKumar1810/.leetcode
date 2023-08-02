#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self,flowerbed, n):
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i-1] == 0:  # Check left adjacency
                    if i == len(flowerbed)-1 or flowerbed[i+1] == 0:  # Check 
                        # right adjacency
                        count += 1
                        i += 2  # Skip the next position since we
                        # have placed a flower
                        continue
            i += 1
            if count >= n:
                return True
        return count >= n


        
# @lc code=end

