#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root,targetSum):
        if not root :
                return False
        if not root.left and not root.right:
            return targetSum - root.val == 0
        return (self.hasPathSum(root.left, targetSum - root.val) 
                    or self.hasPathSum(root.right, targetSum - root.val))
# In last line we are just retutning the value by comapairing with current
#  root.left value with target sum or current root.right value with traget sum 


        
# @lc code=end

