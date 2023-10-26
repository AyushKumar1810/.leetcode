#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        char_count={}
        for char in s :
            char_count[char]=char_count.get(char,0)+1
        sorted_chars = sorted(s, key=lambda x: (-char_count[x], x))
        return ''.join(sorted_chars)
# @lc code=end

