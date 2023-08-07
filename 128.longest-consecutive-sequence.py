#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
#NOTE:our idea is that we will check if the current no -1 (prevuous no for eg is starting arr[i] is 100 then 99 is available in array or not if not then it will be 1st consequtive no and then we will find if current no + 1 exists in array or not if it's then we will increament current no as well as current streak)
class Solution:
    def longestConsecutive(self, nums):
        if not nums :
            return 0
        num_set=set(nums)
        longest_streak=0
        for num in num_set: # suppose num=100
            if num-1 not in num_set:# if 99 is not in num_set then 100 is the 1st value
                current_num=num # we will store in new variable
                current_streak=1
                while current_num + 1 in num_set:#then we will check for next no (as we have to find largest consequetive) i.e 101 is there or not if it's there then we will increamnet the value
                    current_num=current_num + 1
                    current_streak =current_streak +1 
                longest_streak=max(longest_streak,current_streak)
        return longest_streak

        
        
# @lc code=end

