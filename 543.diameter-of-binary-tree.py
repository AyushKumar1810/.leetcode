#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # res=[0]
        # def dfs (root):
        #     if not root:
        #         return -1
        #     left=dfs(root.left)
        #     right=dfs(root.right)
        #     res[0]=max(res[0], 2 + left + right)#for finding diameter
        #     return 1 + max(left,right) # for finding height we are just finding max height of it's left or right node and just adding 1 
        # dfs(root)
        # return res[0]
        self.max_diameter=0
        def depth(node):
            if not node :
                return 0
            left_depth=depth(node.left)
            right_depth=depth(node.right)
            self.max_diameter=max(self.max_diameter , left_depth + right_depth)
            return 1 + max(left_depth, right_depth)
        depth(root)
        return self.max_diameter

# @lc code=end

