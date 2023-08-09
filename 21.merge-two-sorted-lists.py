#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Create a dummy node as the starting point of the merged list
        dummy = ListNode()
    # Create a pointer to keep track of the last node in the merged list
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
            # Attach the node from list1 to the merged list and move list1 pointer
                current.next = list1
                list1 = list1.next
            else:
            # Attach the node from list2 to the merged list and move list2 pointer
                current.next = list2
                list2 = list2.next
        # Move the current pointer to the last node in the merged list
            current = current.next

    # Attach the remaining nodes from list1 or list2 (if any) to the merged list
        current.next = list1 or list2

    # Return the head of the merged linked list (excluding the dummy node)
        return dummy.next
# @lc code=end

