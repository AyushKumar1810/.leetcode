#
# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case Check
        if head is None or head.next is None:
            return None

        slow = head
        fast = head.next.next

        # Two-Pointer Approach to Find the Middle Node
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Delete the Middle Node
        slow.next = slow.next.next

        # Return the Updated Head
        return head
# @lc code=end

