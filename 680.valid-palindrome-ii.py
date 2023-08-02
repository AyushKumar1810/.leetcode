#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0 , len(s)-1
        while l < r:
            if s[l] !=s[r]: # If the 1st and last digit is not equal then 
#it's Not pallindrom but we can deleted one word to make it pallindrom ..
                skipL , skipR = s[l+1:r+1] , s[l:r] # here we are assigning new
#vriable with No first index for skipL and removing last element of the given 
# string 
                return ( skipL ==skipL[::-1] or skipR ==skipR[::-1]) # and we 
#are returning the value after removing the first word or after removing the 
# last word of given string
            l,r = l+1 ,  r-1
        return True
        
# @lc code=end

