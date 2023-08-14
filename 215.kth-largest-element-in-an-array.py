#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap=[]
        for num in nums:
            heapq.heappush(min_heap,num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
        
# @lc code=end

