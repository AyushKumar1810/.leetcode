# 346. Moving Average from Data Stream
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Example:

# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
from collections import deque 
class MovingAverage:  
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.sum = 0
    def next(self, val: int) -> float:
        self.queue.append(val)
        self.sum += val # sum of all elements in the queue 
        if len(self.queue) > self.size: # if the length of the queue is greater than the size of the window , remove the oldest element from the queue and subtract it from the sum 
            self.sum -= self.queue.popleft() # remove the oldest element from the queue 
        return self.sum / len(self.queue) # return the average of the elements in the queue 
