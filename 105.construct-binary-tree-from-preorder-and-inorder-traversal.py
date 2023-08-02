#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#NOTE-Basically we are taking root value from preorder as 1st value of preorder is root , and after that we are just finding where is that value in inorder as on the left of that value of inorder it will be left side of tree and on the right it will be right side of the tree .. 
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder[0]) # Taking Rootnode value from preorder
        mid=inorder.index(preorder[0]) #Assecing rootnoe value position in inorder
        root.left=self.buildTree(preorder[1:mid+1] , inorder[:mid]) # For left subTree we will do recursive and go from 1 to rootnide -1 value  in preorder and same in inorder
        root.right=self.buildTree(preorder[mid+1:] , inorder[mid+1:])
        return root
        
# @lc code=end

