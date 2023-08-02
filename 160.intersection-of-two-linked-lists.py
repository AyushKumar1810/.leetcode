#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# the idea is quite clear if we get l1.next == l2.next then return that
#  intersection value otherwise keep moving pointer of l2 and l2 by l1.next and 
# l2.next
class Solution:
    def getIntersectionNode(self, headA ,headB):
        l1 , l2= headA , headB
        while l1!=l2:
            l1=l1.next if l1 else headB
            l2=l2.next if l2 else headA
        return l1 # if l1 == l2 then
        
# @lc code=end

