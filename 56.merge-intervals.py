#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        intervals.sort()
        ans=[]
        for i in range(n):
            if not ans or intervals[i][0] > ans[-1][1]: # if the intervals is not overlapping then simply add that interval to our answer
                ans.append(intervals[i])
            else:
                ans[-1][1]=max(ans[-1][1] ,intervals[i][1]) # if it's overlapping then take max of two interval 
        return ans
        
# @lc code=end

