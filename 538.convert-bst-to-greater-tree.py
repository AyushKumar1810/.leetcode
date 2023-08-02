#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#NOTE- For solving this question , for root node the value greater than root node will be on right side as it's BST , not only for root node it's valid for any no on binary tree , greater value than that value will be on right side and lessser will beon the left 

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Initialize a variable to keep track of the sum
        curSum = [0]
        
        # Define the recursive helper function
        def dfs(node):
            if not node:
                return None
            
            # Traverse the right subtree
            dfs(node.right)
            
            # Update the node value and curSum
            node.val += curSum[0]
            curSum[0] = node.val
            
            # Traverse the left subtree
            dfs(node.left)
        
        # Start the recursive traversal from the root
        dfs(root)
        
        # Return the modified BST
        return root

        
# @lc code=end

