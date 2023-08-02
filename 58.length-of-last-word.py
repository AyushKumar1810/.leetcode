#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s):
        i=len(s)-1
        length=0
        while s[i] ==" ":#Here we are checking if our pointer gets a empty 
#space then decreament the i value ,means remove the empty space .
            i=i-1
        while i>=0 and s[i]!=" ":# here on the other case we are checking string
            # is not empty and No empty space we would encounter then we will
            # increament length and decreament the i value
            length=length+1
            i=i-1
        return length        
# @lc code=end

