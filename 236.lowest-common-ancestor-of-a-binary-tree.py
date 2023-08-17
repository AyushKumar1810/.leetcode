#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
# Base case: if root is None or one of the nodes is the root, return root

        if root is None or root==p or root==q :
            return root
            # Recurse on the left subtree to find LCA for p and q

        left= self.lowestCommonAncestor(root.left,p,q)
        # Recurse on the right subtree to find LCA for p and q

        right = self.lowestCommonAncestor(root.right,q,p)
        # If one of the subtrees didn't find LCA, return the other

        if left is None:
            return right
        elif right is None:
            return left
        else: # Both subtrees found LCA, so current root is the LCA
            return root
        
# @lc code=end

