#
# @lc app=leetcode id=2220 lang=python3
#
# [2220] Minimum Bit Flips to Convert Number
#

# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_resullt=start^goal
        count = 0
        while xor_resullt:
            count+=xor_resullt & 1 
            xor_resullt>>=1
        return count   

        
# @lc code=end

