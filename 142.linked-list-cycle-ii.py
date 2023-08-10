#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st=set() # we have created a hash set to store the element there 
        while head !=None : # we will check till last node
            if head in st : # If we found the  node in st then we we will return as it will be duplicate 
                return head
            st.add(head) # Otherwise we will add to the st
            head=head.next # And we will move our pointer 
        return None
        
# @lc code=end

