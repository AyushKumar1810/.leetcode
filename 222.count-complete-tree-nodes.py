#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        if left_height == right_height:
            return 2 ** left_height + self.countNodes(root.right)
        else:
            return 2 ** right_height + self.countNodes(root.left)

    def getHeight(self, node):
        return 0 if not node else 1 + self.getHeight(node.left)
# @lc code=end

