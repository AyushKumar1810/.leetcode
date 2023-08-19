#Question :Problem Statement: Children Sum Property in a Binary Tree. Write a program that converts any binary tree to one that follows the children sum property.

# The children sum property is defined as, For every node of the tree, the value of a node is equal to the sum of values of its children(left child and right child).

# Note: 

# The node values can be increased by 1 any number of times but decrement of any node value is not allowed.
# A value for a NULL node can be assumed as 0.
# You are not allowed to change the structure of the given binary tree.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def hasChildrenSumProperty(node):
    if node is None:
        return True
    
    # If both children are None, the property holds
    if node.left is None and node.right is None:
        return True
    
    # Calculate the sum of child values (if they exist)
    left_value = node.left.value if node.left else 0
    right_value = node.right.value if node.right else 0
    
    # Check if the property holds for the current node
    if node.value == left_value + right_value:
        # Recursively check for left and right subtrees
        left_property = hasChildrenSumProperty(node.left)
        right_property = hasChildrenSumProperty(node.right)
        
        # The property holds if both subtrees satisfy it
        return left_property and right_property
    
    return False

# Example usage
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(2)

if hasChildrenSumProperty(root):
    print("The binary tree satisfies the Children Sum Property.")
else:
    print("The binary tree does not satisfy the Children Sum Property.")
