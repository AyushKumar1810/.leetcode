#
# @lc app=leetcode id=2816 lang=python3
#
# [2816] Double a Number Represented as a Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        current = head
        prev = None
        while current:
            current.val = current.val*2 + carry
            carry = current.val//10
            current.val %=10
            prev=current
            current=current.next
        if carry:
            prev.next = ListNode(carry)
        return head

        
# @lc code=end

