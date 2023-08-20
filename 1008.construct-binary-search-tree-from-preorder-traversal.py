#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def construct(lower=float('-inf'), upper=float('inf')):
            nonlocal index
            if index == len(preorder):
                return None
        
            value = preorder[index]
            if value < lower or value > upper:
                return None
        
            index += 1
            node = TreeNode(value)
            node.left = construct(lower, value)
            node.right = construct(value, upper)
            return node
    
        index = 0
        return construct()

# Example usage
# @lc code=end

