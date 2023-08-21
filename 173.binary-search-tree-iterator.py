#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The idea is that we will stores root value to the stack and then we will go to it's bottom left as per inorder , after that we will pop out the element from stack (Top element) and we will check if it's right side element is present or not if it's then we will again to to it's bottom left and reapeat same things . if we don't have right node then we will pop the element from stack 
class BSTIterator:

    def __init__(self, root):
        self.stack=[]
        while root:
            self.stack.append(root) #we are adding Root to the stack 
            root=root.left# then we are going / adding all it;s left element in stack
        

        

    def next(self) -> int:
        res=self.stack.pop() # we are popping  top element one by one from stack after we all added root left node to the stack 
        cur=res.right # also we are checking for right if right node is present then we would gain go to it's left node
        while cur:
            self.stack.append(cur)
            cur=cur.left
        return res.val
        

    def hasNext(self) -> bool:
          return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

