#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#NOTE- we will comapre our Root.value with low and high , if root.val > low and High  then we will delete the Right subtree and we will go to the Left , If root.val is Lower  than  low and high then we will go the Right and delete the Left subTree , so bsaically if our value is in Low to High then good othwewise remove it from the Tree ..
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > high : # So if value is greater than high then we can't move towars right subtree as as value will definetly greater Than root value 
            return self.trimBST(root.left , low , high) # so will Go towards left value and agaian check in the range of Low to high 
         
        if root.val < low :
            return self.trimBST(root.right , low , high )
        # If It's Not greater than High or Less than Low then just update the value 
        root.left=self.trimBST(root.left , low , high)
        root.right=self.trimBST(root.right,low , high)
        return root


        
# @lc code=end

