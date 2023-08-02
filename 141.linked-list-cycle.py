#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#Note - We will solve using Floyd's Tortoise and Hare 
# ( We will choose two Pointer 1 slow , 2nd Fast . slows Moves one step but Fast 
#  Moves Two steps At a Time)

# # class Solution:
# #     def hasCycle(self, head):
# #         slow , fast = head , head
# #         while fast and fast.next:
# #             slow = slow.next # slow moves one step
# #             fast=fast.next.next # fast Moves two steps
# #             if slow==fast: # it will happen when there is a close loop
# #                 return True
# #         return False

#NOTE= Simple solution :

class Solution(object):
    def hasCycle(self, head):
        if not head:  # If the head is None, there is no cycle
            return False
        
        while head.next:  # Traverse the linked list until the next node is None
            if head.val == None:  # If the current node's value is None, it indicates a cycle ( as every value linked to null only)
                return True
            head.val = None  # Mark the current node's value as None to indicate that it has been visited
            head = head.next  # Move to the next node
            
        return False  # If the loop completes without finding a cycle, return False

# @lc code=end

