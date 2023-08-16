class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def top_view(root):
    if root is None:
        return

    # Create a dictionary to store horizontal distance and node values
    hd_dict = {}

    # Queue for level order traversal
    queue = [(root, 0)]

    while queue:
        node, hd = queue.pop(0)

        # If the horizontal distance is not in the dictionary, add it
        if hd not in hd_dict:
            hd_dict[hd] = node.val

        # Enqueue left child with decreased horizontal distance
        if node.left:
            queue.append((node.left, hd - 1))

        # Enqueue right child with increased horizontal distance
        if node.right:
            queue.append((node.right, hd + 1))

    # Print the values from the dictionary
    for val in sorted(hd_dict.keys()):
        print(hd_dict[val], end=" ")

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)
root.left.right.right.right = TreeNode(6)

print("Top view of binary tree:")
top_view(root)
