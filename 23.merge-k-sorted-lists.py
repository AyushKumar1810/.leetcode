#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
            nums=[]
            for i in lists:
                while i:
                    nums.append(i.val)
                    i=i.next
            nums.sort()
            dummy=ListNode()
            tail=dummy
            for i in nums:
                new_node=ListNode(i)
                tail.next=new_node
                tail=tail.next
            return dummy.next       
# @lc code=end

