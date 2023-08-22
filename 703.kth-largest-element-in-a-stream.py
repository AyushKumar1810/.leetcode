#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []  # Min-heap to store the k largest elements
        self.k = k  # The value of k

        # Populate the min_heap with the initial k elements
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Push the value onto the min_heap
        heapq.heappush(self.min_heap, val)

        # If the size of min_heap exceeds k, pop the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The top element of min_heap is the kth largest element
        return self.min_heap[0]

# Example usage
# k = 3
# nums = [4, 5, 8, 2]
# kthLargest = KthLargest(k, nums)
# print(kthLargest.add(3))  # Output: 4 (3rd largest element in [4, 5, 8, 2])
# print(kthLargest.add(5))  # Output: 5 (3rd largest element in [5, 4, 8, 2])
# print(kthLargest.add(10)) # Output: 5 (3rd largest element in [10, 5, 8, 2])
# print(kthLargest.add(9))  # Output: 8 (3rd largest element in [9, 10, 8, 2])
# print(kthLargest.add(4))  # Output: 8 (3rd largest element in [4, 9, 10, 8, 2])

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

