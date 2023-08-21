#Question:Input: N=6
#        Arr=[5,3,6,2,4,1]
#        K=3

# Output: Kth largest element is 4
#         Kth smallest element is 3



# Input: N=7
#        Arr=[10,40,45,20,25,30,50]
#        k=3

# Output: Kth largest element is 4
#         Kth smallest element is 3
# Define the TreeNode class for BST nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Define the kthLargest function to find the Kth largest element in a BST
def kthLargest(root, k):
    # Initialize a stack for the reverse in-order traversal
    stack = []
    
    # Perform reverse in-order traversal until reaching the Kth largest element
    while True:
        # Traverse right until reaching the rightmost leaf
        while root:
            stack.append(root)
            root = root.right
        
        # Pop the node from the stack
        root = stack.pop()
        
        # Decrement K
        k -= 1
        
        # If K becomes 0, return the value of the current node
        if k == 0:
            return root.val
        
        # Move to the left subtree
        root = root.left

# Create a sample BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

# Define the value of K
k = 3

# Call the kthLargest function and store the result
result = kthLargest(root, k)

# Print the result
print(f"The {k}th largest element in the BST is: {result}")
