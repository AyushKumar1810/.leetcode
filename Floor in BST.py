# Define the TreeNode class for BST nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Define the floor function to find the floor value in a BST
def floor(root, key):
    # Base case: if the root is None, return None
    if not root:
        return None
    
    # If the current node's value is equal to the key, return the value
    if root.val == key:
        return root.val
    
    # If the key is smaller than the current node's value, search in the left subtree
    if root.val > key:
        return floor(root.left, key)
    
    # If the key is greater than the current node's value, search in the right subtree
    floor_value = floor(root.right, key)
    
    # If the floor_value is None or greater than the key, return the current node's value
    if floor_value is None or floor_value > key:
        return root.val
    
    # Otherwise, return the floor_value
    return floor_value

# Create a sample BST
root = TreeNode(8)
root.left = TreeNode(4)
root.right = TreeNode(12)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.left = TreeNode(10)
root.right.right = TreeNode(14)

# Define the key for which to find the floor value
key = 5

# Call the floor function and store the result
result = floor(root, key)

# Print the result
print(f"Floor value of {key} in the BST is: {result}")
