#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
#basically we are using binaray search as we have to make solution of O(log(n)).
# class Solution:
#     def searchInsert(self, nums , target ):
#         l=0
#         r=len(nums)-1
#         while l<=r:
#             mid=(l+r)//2
#             if target==nums[mid]:
#                 return mid
#             if target > nums[mid]:
#                 l=mid + 1
#             else :
#                 r=mid -1
#         return l
class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):  #iterating through the list 
            if nums[i] == target: #if target is found in the list then return the index of that element   
                return i 
            if nums[i] > target: #if the element is greater than the target then return the index of that element 
                return i 
        return len(nums) #if the target is greater than all the elements in the list then return the length of the list 

# @lc code=end

