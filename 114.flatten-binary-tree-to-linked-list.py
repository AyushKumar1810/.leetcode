#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return root
            
            # Recursively flatten the left and right subtrees
            left_node = dfs(root.left)
            right_node = dfs(root.right)
            
            # Modify the tree in-place to flatten it
            if root.left:
                root.left = None
                root.right = left_node
                
                # Find the rightmost node of the flattened left subtree
                while left_node.right:
                    left_node = left_node.right
                
                # Attach the flattened right subtree to the rightmost node
                left_node.right = right_node
            
            return root
        
        # Call the helper function to flatten the tree starting from the root
        dfs(root)

        
# @lc code=end

