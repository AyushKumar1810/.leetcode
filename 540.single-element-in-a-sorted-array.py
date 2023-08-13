#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # # num_count={} # we are taking hashmap to count no of time digits repeated 
        # # for num in nums :
        # #     if num in num_count:
        # #         num_count[num]+=1 # If we found duplicate then we will increase it's count
        # #     else :
        # #         num_count[num]=1 # If not Remains 1 
        # # for num , count in num_count.items(): # If count is 1 then return that value 
        # #     if count==1:
        # #         return num
# Now for efficient solution we shall solve it with using Binary to get time complexivity of O(Log(n))
        left , right = 0 , len(nums)-1
        while left  < right :
            mid = left + (right-left)//2
            if mid %2==1:
                mid -=1
            if nums[mid]!=nums[mid+1]:
                right=mid
            else :
                left = mid +2

        return nums[left]
# @lc code=end

