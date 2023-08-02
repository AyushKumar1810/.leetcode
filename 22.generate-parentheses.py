#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def dfs(left,right,s):

            if len(s)==n*2:
                return result.append(s) 
            
            if left<n:
                dfs(left+1,right,s+'(')
            
            if right< left:
                dfs(left,right+1,s+')')
        
        result=[]
        dfs(0,0,'')
        return result
        
# @lc code=end

