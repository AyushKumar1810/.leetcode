#
# @lc app=leetcode id=1750 lang=python3
#
# [1750] Minimum Length of String After Deleting Similar Ends
#

# @lc code=start
#NOTE: The Concept/Approach is quite simple we take left and right left will be at 0 and right will be at last index . After that we will compare left with right if left is equal to right then we will check Left+1 is same as left if it's then we will increament the value of left and same we will do with right and for that we will decreament the pointer . For returning left we will do right - left + 1
class Solution:
    def minimumLength(self, s: str) -> int:
        left , right = 0 , len(s)-1
        while left<right and s[left]==s[right]:
            char=s[left]
            while left <= right and s[left]==char:
                left = left + 1
            while left <=right and s[right] == char:
                right = right-1
        return right -left +1        
# @lc code=end

