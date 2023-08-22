#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []  # Min-heap to store elements greater than median
        self.max_heap = []  # Max-heap to store elements less than or equal to median

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)  # Pushing the negative of num to max_heap
        else:
            heapq.heappush(self.min_heap, num)   # Pushing num to min_heap

        # Balancing the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))  # Moving from max_heap to min_heap
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))  # Moving from min_heap to max_heap

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2  # Calculating median for even number of elements
        else:
            return -self.max_heap[0]  # Median for odd number of elements

# Example usage
# medianFinder = MedianFinder()
# medianFinder.addNum(1)
# medianFinder.addNum(2)
# median = medianFinder.findMedian()
# print(median)  # Output: 1.5
# medianFinder.addNum(3)
# median = medianFinder.findMedian()
# print(median)  # Output: 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

