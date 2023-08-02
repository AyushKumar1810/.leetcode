#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res=[]
        def dfs(node):
            if not node :
                res.append("N")
                return
            res.append(str(node.val)) # If node value is not null then we are adding it to result in a form of string ..
            dfs(node.left) # recursive call to the left node 
            dfs(node.right)# recursive call to the Right node
        dfs(root)
        return ",".join(res) # we are adding each str value with separate of "," . For eg [1,2,3,4,5,6,7,N,N]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i=0
        def dfs ():
            if vals[self.i]=="N":
                self.i+=1
                return None
            node=TreeNode(int(vals[self.i]))
            self.i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

