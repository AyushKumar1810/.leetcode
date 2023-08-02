#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    # Initialize the left and right pointers
        l = 0 
        r = len(nums) - 1

    # Calculate the middle index
        mid = (l + r) // 2

    # Base case: if the left pointer is greater than the right pointer, return None
        if l > r:
            return None

    # Create a new TreeNode with the value at the middle index
        root = TreeNode(nums[mid])

    # Recursively construct the left subtree
        root.left = self.sortedArrayToBST(nums[0:mid])

    # Recursively construct the right subtree
        root.right = self.sortedArrayToBST(nums[mid + 1 : r + 1])

    # Return the root node of the constructed binary search tree
        return root

#Basically we are using Bianary search 

        
# @lc code=end

