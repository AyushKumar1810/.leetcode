#
# @lc app=leetcode id=768 lang=python3
#
# [768] Max Chunks To Make Sorted II
#

# @lc code=start
class Solution:
    def maxChunksToSorted(self,arr):
        n = len(arr)
        max_left = [0] * n
        min_right = [float('inf')] * n

    # Calculate the maximum element on the left for each position
        max_value = float('-inf')
        for i in range(n):
            max_value = max(max_value, arr[i])
            max_left[i] = max_value

    # Calculate the minimum element on the right for each position
        min_value = float('inf')
        for i in range(n - 1, -1, -1):
            min_value = min(min_value, arr[i])
            min_right[i] = min_value

        chunks = 1  # At least one chunk is required
        for i in range(1, n):
        # Check if the maximum element on the left is smaller than or equal to
        # the minimum element on the right for the current position
            if max_left[i - 1] <= min_right[i]:
                chunks += 1

        return chunks

        
# @lc code=end

