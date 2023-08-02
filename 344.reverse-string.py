#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.        
        """



        # 1 iterative solution with space O(1)
# we are just swapping left =0th index with the right = last index and
# the swapping continue till L<R
        l,r=0,len(s)-1
        while l < r:
            s[l] , s[r] = s[r] , s[l]
            l,r=l+1 , r-1
        # 2 stack solution with extra space O(n)
# The basic idea we will use here is that we will put all the s string into
#  stack as we know that stack follows LIFO so after that we will pop all the 
# strating from stack To s
        stack=[]
        for c in s :
            stack.append(c)
        i=0    
        while stack:
            s[i]=stack.pop()
            i=i+1

        # 3  Recurcive solution :
        
        def reverse ( l,r):
            if l<r:
                s[l] , s[r] = s[r] , s[l]
                reverse( l+1 , r-1)
        reverse ( 0 , len(s) - 1    )
# @lc code=end

