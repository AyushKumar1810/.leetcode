#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
# taking two pointers One from 1th index and other from the last index 
# we will keep increament out left pointer by 1 and decreament our right pointer by 1 , if l!=r then return fasle 
        
        l=0 #starting from the initial 
        r=len(s)-1 #starting from the right side 
        while l<r:
            while l < r and not self.alphaNum(s[l]):
                l=l+1
            while l < r and not self.alphaNum(s[r]):
                r=r-1
            if s[l].lower()!=s[r].lower():
                return False
            l,r=l+1 , r-1
        return True
    def alphaNum(self,c):
        return (ord('A')<=ord(c)<= ord('Z') or
                ord('a')<=ord(c)<=ord('z') or
                ord('0')<=ord(c)<=ord('9'))
        
# @lc code=end

