#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth=0
        max_depth=0
        for char in s :
            if char == "(":
                current_depth =current_depth +1
                max_depth=max(max_depth , current_depth)
            elif char ==")":
                current_depth-=1
        return max_depth

        
# @lc code=end

