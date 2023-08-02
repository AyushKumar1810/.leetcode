#
# @lc app=leetcode id=456 lang=python
#
# [456] 132 Pattern
#

# @lc code=start
class Solution(object):
    def find132pattern(self,nums):
        prev_min = float('inf')
        stack = []
        for n in nums:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n > stack[-1][1]:
                return True
            stack.append([n, prev_min])
            prev_min = min(prev_min, n)
        return False

        
# @lc code=end

