#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        # Find the middle of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Divide the list into two halves
        middle = slow.next
        slow.next = None
        
        # Recursively sort the two halves
        left = self.sortList(head)
        right = self.sortList(middle)
        
        # Merge the sorted halves
        return self.merge(left, right)
    
    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        
        if left.val < right.val:
            left.next = self.merge(left.next, right)
            return left
        else:
            right.next = self.merge(left, right.next)
            return right

# NOTE= It's just a Merge sort

        
# @lc code=end

