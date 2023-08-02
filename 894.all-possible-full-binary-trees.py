#
# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        def backtrack(n):
            if n == 0:
                return []  # Base case: If n is 0, return an empty list
            if n == 1:
                return [TreeNode()]  # Base case: If n is 1, return a single TreeNode

            if n % 2 == 0:  # Check if n is even, return empty list
                return []

            res = []  # List to store all possible FBTs

            # Try all possible combinations of left and right subtree sizes
            for left in range(n):
                right = n - left - 1

                # Recursively generate all possible left and right subtrees
                leftTree = backtrack(left)
                rightTree = backtrack(right)

                # Combine each left subtree with each right subtree to form FBTs
                for t1 in leftTree:
                    for t2 in rightTree:
                        res.append(TreeNode(0, t1, t2))

            return res

        return backtrack(n)



        
# @lc code=end

