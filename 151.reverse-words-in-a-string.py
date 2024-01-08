#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
#We will splits every words of s 
        words = s.split()
    # Reverse the list of words and join them back into a string
        reversed_words = ' ' .join(reversed(words))
        return reversed_words

        
# @lc code=end

