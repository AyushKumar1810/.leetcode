#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#NOTE- So we will use of queue data structure , we will create two variable one  queue to store value and other res to store our right side of tree .. 
# so we will traverse from the root , we will put root to the queue  , before adding another value like we will go with BFS (level over {Horizontally from left to right }) we have to pop top of the queue , so we will pop and add to our res , then we will add node value left right ..
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # Initialize an empty list to store the right side view values

        if not root:
            return res  # If the root is None (empty tree), return the empty result list

        queue = [root]  # Create a queue and add the root node to it

        while queue:
    # Iterate through the elements in the queue (process one level of the tree at a time)
            for n in range(len(queue)):
                first_val = queue.pop(0)  # Pop the first element from the queue

        # If n is 0, it means this is the rightmost node at the current level
        # Append its value to the result list
                if n == 0:
                    res.append(first_val.val)

        # Add the right child of the current node to the queue
                if first_val.right:
                    queue.append(first_val.right)

        # Add the left child of the current node to the queue
                if first_val.left:
                    queue.append(first_val.left)

        return res  # Return the result list containing the right side view values

        
# @lc code=end

