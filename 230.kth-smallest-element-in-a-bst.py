#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        return ans[k-1]
        # stack=[]
        # while True :
        #     while root:
        #         stack.append(root)
        #         root=root.left
        #     root=stack.pop()
        #     k=k-1
        #     if k==0:
        #         return root.val
        #     root=root.val

# here i am performing inorder traversal, hence giving me sorted array        
# @lc code=end

