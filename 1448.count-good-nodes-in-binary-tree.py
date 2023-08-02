#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root):
        # Define a recursive helper function dfs
        def dfs(node , maxVal):
            # Check if the node is None (base case)
            if not node :
                return 0
            # Check if the value of the node is greater than or equal to the current maxVal
            res = 1 if node.val >= maxVal else 0 
            # Update the maxVal to the maximum of current maxVal and node value
            maxVal = max(maxVal , node.val)
            # Recursively call dfs on the left child of the current node and add the result to res
            res += dfs(node.left, maxVal)
            # Recursively call dfs on the right child of the current node and add the result to res
            res += dfs(node.right, maxVal)
            # Return the final result
            return res
        
        # Call the dfs function with the root node and the value of root.val as the starting maxVal
        return dfs(root, root.val)

        
# @lc code=end

