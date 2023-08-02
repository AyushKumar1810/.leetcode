#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#NOTE- The idea we are using is that we have to rob the level of tree with skipping adjecent node , inshort either in even or odd order , so if we are selecting root value then we have to selecting node whivh is of height 2 from root , if we are selecting child of root then we have to skip it's next value and so on ..
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return (0, 0)  # (rob_current, rob_next)

            left = helper(node.left) #DFS on LEFT SUB TREE
            right = helper(node.right) #DFS on RIGHT SUB TREE

            # Calculate the maximum amount of money that can be robbed
            # from the current node and its grandchildren
            rob_current = node.val + left[1] + right[1] # With Rootnode , we have to take root value + skipping (left[0] and right[0]) value and taking next node 

            # Calculate the maximum amount of money that can be robbed
            # from the next level nodes
            rob_next = max(left) + max(right)

            return (rob_current, rob_next)

        result = helper(root)
        return max(result)

# Example usage:
# root = TreeNode(3)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(3)
# root.right.right = TreeNode(1)

# solution = Solution()
# max_money = solution.rob(root)
# print("Maximum amount of money that can be robbed:", max_money)

        
# @lc code=end

