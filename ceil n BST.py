# Define the TreeNode class for BST nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Define the ceil function to find the ceiling value in a BST
def ceil(root, key):
    # Base case: if the root is None, return None
    if not root:
        return None
    
    # If the current node's value is equal to the key, return the value
    if root.val == key:
        return root.val
    
    # If the key is greater than the current node's value, search in the right subtree
    if root.val < key:
        return ceil(root.right, key)
    
    # If the key is smaller than the current node's value, search in the left subtree
    ceil_value = ceil(root.left, key)
    
    # If the ceil_value is None or less than the key, return the current node's value
    if ceil_value is None or ceil_value < key:
        return root.val
    
    # Otherwise, return the ceil_value
    return ceil_value

# Create a sample BST
root = TreeNode(8)
root.left = TreeNode(4)
root.right = TreeNode(12)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.left = TreeNode(10)
root.right.right = TreeNode(14)

# Define the key for which to find the ceil value
key = 5

# Call the ceil function and store the result
result = ceil(root, key)

# Print the result
print(f"Ceil value of {key} in the BST is: {result}")
