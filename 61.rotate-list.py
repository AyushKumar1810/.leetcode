#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head,k):
        if not head : 
            return head
    # Get length
        length , tail =1 , head # we have make length to 1 , 
        # it will be one head and tail will be at same position
        while tail.next: # Untill Null
            tail=tail.next # we will move head pointer untill it reches null
            length+=1 # As it coves we increase length so we can count length
        k = k%length # For finding it's k we will use mod 

        if k==0:
            return head
        curr=head #we will assign curr to head value
        for i in range(length-k-1): # we will go till the index of that 
            curr=curr.next # increament head value 
        newHead=curr.next # storing it 
        curr.next=None #then once it will reach to null
        tail.next=head # we will swap as it's rotaion and make tail value to head
        return newHead
        
# @lc code=end

