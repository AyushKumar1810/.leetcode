#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#NOTE:using Tortoise-Hare-Approach
#Approach: 

# Create two pointers slow and fast and initialize them to a head pointer.
# Move slow ptr by one step and simultaneously fast ptr by two steps until fast ptr is NULL or next of fast ptr is NULL.
# When the above condition is met, we can see that the slow ptr is pointing towards the middle of the Linked List and hence we can return the slow pointer.
# In that we will two pointer slow and fast , slow moves one step at a time and fast moves two steps a time , so when fast reaches at the end so slow will be half way i.e it will be in the middle..
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
        while fast and fast.next:
            slow , fast= slow.next , fast.next.next
        return slow
# @lc code=end

