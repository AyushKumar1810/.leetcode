#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum path sum variable
        self.res = float('-inf')
        
        # Helper function for DFS traversal
        def dfs(root):
            # Base case: if node is None, return 0
            if not root:
                return 0
            
            # Recursively calculate the maximum sum of the right subtree
            right = max(dfs(root.right), 0) # 1If dfs(root.right) returns a positive value (greater than 0), we assign that value to right.
# 2 If dfs(root.right) returns 0 or a negative value, we assign 0 to right.
            
            # Recursively calculate the maximum sum of the left subtree
            left = max(dfs(root.left), 0) # same apply to the left
            
            # Calculate the maximum path sum passing through the current node
            current_sum = root.val + left + right
            
            # Update the global maximum path sum
            self.res = max(self.res, current_sum)
            
            # Return the maximum sum of the current node and either left or right subtree
            return root.val + max(left, right)
        
        # Call the helper function on the root node
        dfs(root)
        
        # Return the maximum path sum
        return self.res
        
# @lc code=end

