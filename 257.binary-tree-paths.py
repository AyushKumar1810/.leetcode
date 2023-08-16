#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node , path):
            if not node :
                return 
            path.append(str(node.val))
            if not node.left and not node.right :
                paths.append("->".join(path))      
            else:
                dfs(node.left , path.copy())
                dfs(node.right,path.copy())  
        paths=[]
        dfs(root,[])
        return paths
# @lc code=end

