#
# @lc app=leetcode id=853 lang=python
#
# [853] Car Fleet
#

# @lc code=start
class Solution(object):
    def carFleet(self,target, position, speed):
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
    
        for p, s in sorted(pair):
            eta = (target - p) / s
        
            if not stack:
                stack.append(eta)
            else:
                while stack and eta >= stack[-1]:
                    stack.pop()
                stack.append(eta)
    
        return len(stack)

    
        
# @lc code=end

