#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, row, col):
            if not node:
                return
            cols[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        cols = defaultdict(list)
        dfs(root, 0, 0)

        result = []
        for col in sorted(cols.keys()):
            col_values = [val for row, val in sorted(cols[col])]
            result.append(col_values)

        return result

            


# @lc code=end

