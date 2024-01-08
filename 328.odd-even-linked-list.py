#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Check if the linked list is empty or has only one node
        if not head or not head.next:
            return head
    # Initialize pointers for odd and even nodes
        odd_head=head
        even_head=head.next
    # Initialize pointers to traverse odd and even nodes separately
        odd=odd_head
        even=even_head
        while even and even.next:
        #Connect Odd Nodes
            odd.next=even.next
            odd=odd.next
        #Connect Even Nodes
            even.next=odd.next
            even=even.next
        # Attach the even list after the odd list
        odd.next=even_head
        return odd_head



# @lc code=end

