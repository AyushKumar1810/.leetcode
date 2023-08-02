class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset=set() # we are using set
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in charset: # if that character is alreday present then remove the duplicate character
                charset.remove(s[l]) # remove it
                l+=1
            charset.add(s[r]) # If not duplicate then add 
            res = max(res,r-l+1) # update the result with it's present max ofr with length bewtween r and l character
        return res
