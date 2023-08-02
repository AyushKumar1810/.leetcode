#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Create a dummy node to handle the case when left = 1

        # Step 1: Reach the node at position "left"
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        # Now cur points to the node at position "left", and leftPrev points to the node before it

        # Step 2: Reverse the sublist from position "left" to position "right"
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        # Step 3: Update the pointers to reconnect the reversed sublist
        leftPrev.next.next = cur  # Connect the node after "right" to the current node
        leftPrev.next = prev  # Connect the node before "left" to the last node of the reversed sublist

        return dummy.next


        
# @lc code=end

