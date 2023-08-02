#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#NOTE-We can use DFS On both left hand and right hand then we will get it's height wether it's Balanced or not , but it will fetch O(n^2)
#so instead of using it we will use it to right  side  first and find it's height and then we will substract Height of root.left with root.right to get it's parents node wether it's balanced or not , as height difference should not be greater than 1

class Solution:
    def isBalanced(self, root):
        res = [1]  # A list to store the result (1: Balanced, 0: Not Balanced)
        
        def maxDepth(root):
            if not root:
                return 0
            
            # Recursively calculate the maximum depth of the left and right subtrees
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            
            # Check if the absolute difference between the depths of left and right subtrees is greater than 1
            if abs(left - right) > 1:
                res[0] = 0  # If the tree is not balanced, set the result to 0
            
            # Return the maximum depth of the current subtree
            return 1 + max(left, right)
        
        # Call the maxDepth function to check if the tree is balanced
        maxDepth(root)
        
        # Return True if the tree is balanced (res[0] == 1), otherwise return False
        return True if res[0] == 1 else False

        
# @lc code=end

