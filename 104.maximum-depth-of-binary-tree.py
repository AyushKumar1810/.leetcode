#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#NOTE-firstly we will do it by recursively
        # Check if the root node is None, i.e., the tree is empty
        if not root:
            return 0
        
        # If the root node is available, the minimum height will be 1
        # Recursively calculate the maximum depth of the left and right subtrees
        # and return the maximum of the two depths plus 1 for the root node
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#NOTE- Now by using BFS (level order traversal) , we will go level by level like stair case horizontally we will go until we find leaf Node .
#NOTE- the concept of BFS is that we will use a Queue to store tree value , Firstly we will put root Node value into it and then before romoving it from Queue we will check it;s children is on the tree or not if it's then we wil remove it and add it's children into the queue , basically adding a element then checeking it's child is available on tree or not if it's available then add into quque and remove then parent...


        
# @lc code=end

