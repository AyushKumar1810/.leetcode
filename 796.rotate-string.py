#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start

#NOTE:Explanation:

# First, we check if the lengths of both strings A and B are not equal. If they are not equal, it's impossible to obtain B by rotating A, so we return False.

# We then check if B is a substring of the concatenation of A and A. If it is, that means B can be obtained by rotating A, and we return True.

# If B is not found in the concatenated string, we return False.
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if goal in s + s :
            return True
        return False
#NOTE:We first check if the lengths of both strings A and B are equal. In this case, both strings have a length of 5, so the lengths are equal.

# We then check if B is a substring of the concatenation of A and A. The concatenated string is "abcdeabcde".

# We find that B is indeed a substring of the concatenated string, so we return True.

# Output: True
# @lc code=end

