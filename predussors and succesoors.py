#Question :There is BST given with the root node with the key part as an integer only. You need to find the in-order successor and predecessor of a given key. If either predecessor or successor is not found, then set it to NULL.

# NOTE:- In an inorder traversal the number just smaller than the target is the predecessor and the number just greater than the target is the successor. 
# Example 1:

# Input:
#         10
#       /   \
#      2    11
#    /  \ 
#   1    5
#       /  \
#      3    6
#       \
#        4
# key = 8
# Output: 
# 6 10
# Explanation: 
# In the given BST the inorder predecessor of 8 is 6 and inorder successor of 8 is 10.
class TreeNode:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def findPredecessorSuccessor(root, key):
    successor = None
    predecessor = None
    
    while root:
        if key < root.key:
            successor = root
            root = root.left
        elif key > root.key:
            predecessor = root
            root = root.right
        else:
            # Node with key equal to the target key found
            # Find the predecessor (largest node in the left subtree)
            if root.left:
                temp = root.left
                while temp.right:
                    temp = temp.right
                predecessor = temp
            
            # Find the successor (smallest node in the right subtree)
            if root.right:
                temp = root.right
                while temp.left:
                    temp = temp.left
                successor = temp
            
            break
    
    return predecessor, successor

# Example usage
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right.left = TreeNode(25)
root.right.right = TreeNode(35)

key = 15
predecessor, successor = findPredecessorSuccessor(root, key)

if predecessor:
    print("Predecessor:", predecessor.key)
else:
    print("Predecessor: None")

if successor:
    print("Successor:", successor.key)
else:
    print("Successor: None")
