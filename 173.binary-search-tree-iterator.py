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
class BSTIterator:

    def __init__(self, root):
        self.stack=[]
        while root:
            self.stack.append(root)
            root=root.left
        

        

    def next(self) -> int:
        res=self.stack.pop()
        cur=res.right
        while cur:
            self.stack.append(cur)
            cur=cur.left
        return res.val
        

    def hasNext(self) -> bool:
        return self.stack!=[]


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

