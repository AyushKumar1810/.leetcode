#
# @lc app=leetcode id=1903 lang=python3
#
# [1903] Largest Odd Number in String
#

# @lc code=start
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""
        
# @lc code=end

