#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
     
        if not root:
            return 0
    
        max_width = 0
        queue = [(root, 0)]  # Store nodes along with their positions
    
        while queue:
            level_size = len(queue)
            _, first_pos = queue[0]  # Get the position of the first node in the current level

            for _ in range(level_size):
                node, pos = queue.pop(0)
            
            # Update max width using the position of the current node and the first node
                max_width = max(max_width, pos - first_pos + 1)
            
                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))
    
        return max_width

# Example usage
# root = TreeNode(1)
# root.left = TreeNode(3)
# root.right = TreeNode(2)
# root.left.left = TreeNode(5)
# root.left.right = TreeNode(3)
# root.right.right = TreeNode(9)

# print("Maximum width of binary tree:", widthOfBinaryTree(root))

        
# @lc code=end

