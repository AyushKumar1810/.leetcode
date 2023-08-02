#
# @lc app=leetcode id=71 lang=python
#
# [71] Simplify Path
#

# @lc code=start
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        new_path=path.split('/')
        for c in new_path :
            if c=="..":
                if stack:
                     stack.pop()
            elif c and c!='.':
                stack.append(c)
        return '/' +'/'.join(stack)
        
# @lc code=end

