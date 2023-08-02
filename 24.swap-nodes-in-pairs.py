#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        self.swap(head)
        self.swapPairs(head.next.next)
        
        return head
    
    def swap(self, head: ListNode) -> None:
        nextValue = head.next.val
        head.next.val = head.val
        head.val = nextValue

        
        
# @lc code=end

