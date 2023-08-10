#
# @lc app=leetcode id=61 lang=ruby
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @param {Integer} k
# @return {ListNode}
# def rotate_right(head, k):
#     class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def rotateRight(self , head, k):
    # Calculate the length of the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    # Handle cases where the list is empty or has only one node
    if length == 0 or k % length == 0:
        return head
    
    # Find the new head position after rotation
    k %= length
    steps_to_new_head = length - k
    new_head = head
    for _ in range(steps_to_new_head - 1):
        new_head = new_head.next
    
    # Update pointers to achieve the rotation
    new_tail = new_head
    while new_tail.next:
        new_tail = new_tail.next
    new_tail.next = head
    head = new_head.next
    new_head.next = None
    
    return head

    

# @lc code=end

