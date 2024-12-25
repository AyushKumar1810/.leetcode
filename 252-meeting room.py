# 252. Meeting Rooms
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# Example 1:

# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:

# Input: [[7,10],[2,4]]
# Output: true
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
class Solution:
  def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
    intervals.sort() # sort the intervals by the start time example [[0,30],[5,10],[15,20]] -> [[0,30],[5,10],[15,20]] 

    for i in range(1, len(intervals)):
      if intervals[i - 1][1] > intervals[i][0]: # if the end time of the previous interval is greater than the start time of the current interval , return False example [[0,30],[5,10],[15,20]] -> [[0,30],[5,10],[15,20]] 30 > 5 , 10 > 15 , 20 > 0 
        return False # if the previous condition is met , return False 

    return True # if the previous condition is not met , return True  example [[7,10],[2,4]] -> [[2,4],[7,10]] 10 < 2 , 4 < 7 , 7 < 10  True 