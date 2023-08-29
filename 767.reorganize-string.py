#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count the occurrences of each character in the string
        count = Counter(s)
        
        # Create a max heap of pairs: [count, character]
        # Using negative count to achieve max heap behavior
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)  # Convert the list to a max heap
        
        prev = None  # Initialize the previous character
        res = ""     # Initialize the result string
        
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""  # If there's a previous character but the heap is empty, return an empty string
            
            cnt, char = heapq.heappop(maxHeap)  # Get the most frequent character
            res += char                          # Add it to the result
            cnt += 1                             
            
            if prev:
                heapq.heappush(maxHeap, prev)  # Put the previous character back into the heap
                prev = None
            if cnt != 0:
                prev = [cnt, char]  # Update the previous character
            
        return res  # Return the reorganized string
        
        
# @lc code=end

