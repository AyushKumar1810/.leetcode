#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#NOTE- In question we only have to find 1st value of last row ..  we will use BFS To traverse via queue  
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q=deque([root]) #storing root value to the queue
        while q :
            node=q.popleft() # removing root value from q and we will add into q it's child 
            if node.right : q.append(node.right) # we have add right child
            if node.left: q.append(node.left) # And Then left
        return node.val

        
# @lc code=end

