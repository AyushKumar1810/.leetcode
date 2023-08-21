#
# @lc app=leetcode id=1373 lang=python3
#
# [1373] Maximum Sum BST in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
         # Define a helper function to traverse and validate each node
        def dfs(node):
            if not node:
                return float('inf'), float('-inf'), 0, True
            
            # Recursively traverse left and right subtrees
            l_min, l_max, l_sum, l_valid = dfs(node.left)
            r_min, r_max, r_sum, r_valid = dfs(node.right)
            
            # Check if the current subtree is a valid BST
            is_bst = l_valid and r_valid and l_max < node.val < r_min
            
            # Calculate the sum of the current subtree
            subtree_sum = l_sum + r_sum + node.val if is_bst else 0
            
            # Update the maximum sum if the current subtree is a valid BST and has a greater sum
            self.max_sum = max(self.max_sum, subtree_sum)
            
            # Return the minimum, maximum, and sum of the current subtree, along with BST validity
            return min(l_min, node.val), max(r_max, node.val), subtree_sum, is_bst
        
        dfs(root)  # Start the traversal and validation
        
        return self.max_sum  # Return the maximum sum of a BST
# @lc code=end

