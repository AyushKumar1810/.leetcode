#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start

#NOTE: we have given an array and sliding window of size k , and we have to find maximum value in each sliding value  , 
from collections import deque


class Solution:

    def maxSlidingWindow(self , nums, k):
        li = deque()
        ans = []
        i, j = 0, 0

        while j < len(nums):

            while li and li[-1] < nums[j]:
                li.pop()

            li.append(nums[j])

            if j - i + 1 < k:
                j += 1

            elif j - i + 1 == k:
                ans.append(li[0])

                if nums[i] == li[0]:
                    li.popleft()
                i += 1
                j += 1

        return ans

        
# @lc code=end

