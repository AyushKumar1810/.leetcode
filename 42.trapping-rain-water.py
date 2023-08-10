#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        res=0
        maxLeft=0
        maxRight=0
        while left <= right :
            if height[left] <=height[right]:
                if height[left] > maxLeft:
                    maxLeft=height[left]
                else :
                    res+=maxLeft - height[left]
                left = left +1 
            else:
                if height [right] >=maxRight:
                    maxRight=height[right]
                else :
                    res+=maxRight - height[right]
                right-=1
        return res
        
# @lc code=end

