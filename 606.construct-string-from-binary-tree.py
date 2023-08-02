#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root ):
        res=[]
        def preorder(root):
            if not root :
                return 
            res.append("(") # 1st add '(' Then add some value
            res.append(str(root.val))
            if not root.left and root.right:
                res.append("()") # if It's leaf node {no child} then append "()"
            preorder(root.left)
            preorder(root.right)
            res.append(")") # After fininshing add ")" for closing 
        preorder(root)
        return  "".join(res)[1:-1]    
        
# @lc code=end

