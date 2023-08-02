#
# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#NOTE- The idea we acn use here is that if root.left 1 is equal to root.right2 then we can swap as then they will equal 
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2 :
            return not root1  and not root2
        if root1.val !=root2.val: # root value is not equal
            return False 
        a=self.flipEquiv(root1.left , root2.left ) and self.flipEquiv(root1.right,root2.right) # if left side of root1 is equal to left side of root2 and if right side of root1 is equal to right side og root 2 then the tree is equal ..
        return a or self.flipEquiv(root1.left , root2.right ) and self.flipEquiv(root1.right,root2.left) # if not true then we have to swap
# @lc code=end

