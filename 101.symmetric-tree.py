#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

    # #     if not root:
    # #         return True
        
    # #     # Call the helper function to check symmetry of left and right subtrees
    # #     return self.checkSymmetry(root.left, root.right)
    
    # # def checkSymmetry(self, left: TreeNode, right: TreeNode) -> bool:
    # #     # Base case: If both nodes are None, they are symmetric
    # #     if not left and not right:
    # #         return True
    # #     # If one node is None while the other is not, they are not symmetric
    # #     if not left or not right:
    # #         return False
    # #     # Nodes must have equal values and the subtrees must be symmetric
    # #     return (left.val == right.val) and \
    # #            self.checkSymmetry(left.left, right.right) and \
    # #            self.checkSymmetry(left.right, right.left)

# # Example usage
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(3)

# solution = Solution()
# print("Is the tree symmetric?", solution.isSymmetric(root))


        if root is None:
            return True
        return checkSymmetry(root.left, root.right)

def checkSymmetry(left, right):
    if left is None or right is None:
        return left == right
    return (left.data == right.data) and checkSymmetry(left.left, right.right) and checkSymmetry(left.right, right.left)

# Example usage



        
# @lc code=end

