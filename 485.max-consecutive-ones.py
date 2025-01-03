#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
#NOTE:Approach:  We maintain a variable count that keeps a track of the number of consecutive 1’s while traversing the array. The other variable max_count maintains the maximum number of 1’s, in other words, it maintains the answer.

# We start traversing from the beginning of the array. Since we can encounter either a 1 or 0 there can be two situations:-

# If  the value at the current index is equal to 1 we increase the value of count by one. After updating  the count variable if it becomes more than the max_count  update the max_count.
# If the value at the current index is equal to zero we make the variable count as 0 since there are no more consecutive ones.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0  # to store the maximum number of 1's  in the array
        count = 0 # to store the number of consecutive 1's in the array 
        for i in nums:
            if i == 1:
                count += 1
                max_count = max(max_count, count)# to store the maximum number of 1's in the array 
            else:
                count = 0
        return max_count
        
# @lc code=end

