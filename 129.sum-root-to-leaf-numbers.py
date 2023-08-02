#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(curr,num):
            if not curr:
                return 0
            num = num *10 + curr.val
            if not curr.left  and not curr.right :
                return num
            return dfs(curr.left,num) + dfs(curr.right, num) 
        return dfs(root,0)
# we are Doing this "num *10" as we have to count sum as For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123. so if we are going to path 1, 2, 3 then it result will be 123 , but hwo we can add them ? so simply by multiplyng the 1st value by 10 then adding it to next value and again multiply by 10 to results and add with 3rd value .. 
# for eg if we have tree    1
#                          / \
#                         2   3
                        # 0*10+1=1 # we are traversing left node
                        # 1*10+2=12  
# @lc code=end

