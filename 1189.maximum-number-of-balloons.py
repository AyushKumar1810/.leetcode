#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counttext=Counter(text)
        balloon=Counter("balloon")
        res = len(text)
        for i in balloon:
            res = min (res , counttext[i]//balloon[i])
        return res

        
# @lc code=end

