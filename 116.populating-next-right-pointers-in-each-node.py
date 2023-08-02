#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr,next=root,root.left if root else None # initially Curr is At Root Node and Next is at his left children at 1st level 
        while curr and next : 
            curr.left.next=curr.right # we are linked to left to right children
            if curr.next:
                curr.right.next=curr.next.left #The statement curr.right.next = curr.next.left is used to establish the next pointers between nodes in a binary tree level by level. It connects the right child of the current node to the left child of the next node in the same level.
 #FOR E.g        A                 
        #       / \
     #         B   C
       #      / \   \
        #    D  E   F

#Will become:  A
    #         / \
   #         B -> C
  #         / \   \
 #         D -> E -> F       





            curr=curr.next
            if not curr:
                curr=next

                next=curr.left
        return root

        
# @lc code=end

