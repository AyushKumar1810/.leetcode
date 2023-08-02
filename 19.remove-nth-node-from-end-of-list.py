#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head , n ):
        # Step 1: Create two pointers, slow and fast, and initialize them to the head of the linked list.
        slow = fast = head
        
        # Step 2: Move the fast pointer n steps ahead in the linked list.
        for i in range(n):
            if  fast  is None:
                # If the fast pointer reaches the end before moving n steps, it means n is greater than the length of the linked list.
                # In this case, we can return the original head as no node needs to be removed.
                return head
            fast = fast.next
        
        # Step 3: Move both the slow and fast pointers simultaneously until the fast pointer reaches the end of the linked list.
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Step 4: At this point, the slow pointer is pointing to the node just before the node to be removed.
        # We update the next pointer of the slow node to skip the next node, effectively removing it from the linked list.
        slow.next = slow.next.next
        
        # Step 5: Return the head of the modified linked list.
        return head



        
# @lc code=end

