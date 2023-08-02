#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq as heapq
class Solution:
    def lastStoneWeight(self, stones):
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first=heapq.heappop(stones)
            second=heapq.heappop(stones)
            if second> first:
                heapq.heappush(stones,first-second)#we are adding difference to 
                #in the stones 
        stones.append(0)
        return abs(stones[0])
# @lc code=end

