#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#We will use concept of BFS adn we will store in a queue    
# Our approach will be we will go root node and append to The queue and just after removing from the queue and adding it to result we have to append it's children into queue and again doings same things

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        q = collections.deque()
        q.append(root)
        while q:
            qLen=len(q)
            level=[]
            for i in range(qLen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
# @lc code=end

