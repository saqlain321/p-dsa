class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.thread = None  # Pointer to the inorder successor

def populate_threads(root, prev):
    if root:
        populate_threads(root.left, prev)
        if prev[0]:
            prev[0].thread = root
        prev[0] = root
        populate_threads(root.right, prev)

def inorder_traversal_threaded(root):
    current = root
    while current.left:
        current = current.left

    while current:
        print(current.val, end=" ")
        if current.thread:
            current = current.thread
        else:
            current = current.right

# Example usage:
# Constructing a sample binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Populate threads
prev = [None]
populate_threads(root, prev)

print("Inorder Traversal:")
inorder_traversal_threaded(root)  # Output: 4 2 5 1 3
