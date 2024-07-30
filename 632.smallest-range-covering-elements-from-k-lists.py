#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#

# @lc code=start
from collections import defaultdict
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        temp = []
        for i, arr in enumerate(nums):
            for n in arr:
                temp.append((n, i))

        temp.sort()

        k = len(nums)
        ans = (temp[0][0], temp[-1][0])
        best = temp[-1][0] - temp[0][0]

        seen = defaultdict(int)
        start = 0
        for i, (x, idx) in enumerate(temp):
            seen[idx] += 1
            if i == 0:
                continue

            if len(seen) < k:
                continue
            else:
                while len(seen) == k:
                    if x - temp[start][0] < best:
                        best = x - temp[start][0]
                        ans = (temp[start][0], x)
                    
                    y = temp[start][1]
                    seen[y] -= 1
                    if seen[y] == 0:
                        del seen[y]
                    start += 1

        return ans
        
# @lc code=end

