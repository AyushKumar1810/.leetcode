#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q : #If Both tree Not available 
            return True
        if not p or not q or p.val != q.val : # If one of the tree exist and other not and if their value is not equal 
            return False
        return (self.isSameTree(p.left,q.left) and 
                self.isSameTree(p.right,q.right)) # We are doing recursively on both of the tree on left side and right side 



                                        
# @lc code=end

