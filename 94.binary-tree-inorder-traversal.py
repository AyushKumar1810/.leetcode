#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        # Recursive solution 
        # res=[]
        # def inorder(root):
        #     if not root :
        #         return
        #     inorder(root.left)
        #     res.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # return res
        # iterative solution 
        result=[]
        stack=[]
        current=root
        while current or stack :
            while current:
                stack.append(current)
                current= current.left
            current=stack.pop()
            result.append(current.val)
            current=current.right
        return result

# @lc code=end

