#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#

# @lc code=start
# class Solution:
#     def maxChunksToSorted(self, arr: List[int]) -> int:
        
#         chunks = 0
#         max_value = 0

#         for i, num in enumerate(arr):
#             max_value = max(max_value, num)

#             if max_value == i:
#                 chunks += 1

#         return chunks
    

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt, right_bound =0, 0  
        for i, val in enumerate(arr):
            if val > i: 
                right_bound = max(right_bound, val)
            elif val == i and right_bound <= i:
                cnt += 1 
                right_bound = i 
            elif val < i and right_bound == i:
                cnt += 1 
        return cnt 


#  1 3 0 2 
#  0 1 2 3 
#  cnt = 0 
#  val > pos  
#  right_bound = max(right_bound, val (pos) ) 
#
#  val == pos and right_bound <= pos 
#  cnt += 1, right_bound += 1 
#
#  val == pos and right_bound > pos 
#  continue 
#
#  val < pos and right_bound == pos 
#  cnt += 1 
# 
#  val < pos and right_bound > pos 
#  continue 
#
        
# @lc code=end

