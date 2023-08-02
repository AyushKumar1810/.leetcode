#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None
        
        back = head # we are storing 1st head value in it 
        front = head.next # we are storing 2nd value of linked list i.e head.next
        
        while front:
            if front.val != back.val:# if 1st value not equal to 2nd value 
                # in the linked list 
                back = back.next #then we will increament the pointer 
            
            front = front.next
            back.next = front
        
        return head

        
# @lc code=end

