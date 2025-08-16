"""
Problem:
 Given a binary search tree (BST) and an integer k, 
 find the kth smallest element (1-indexed) in the BST. 
 The inorder traversal of a BST yields nodes in ascending order, 
 so the kth visited node is the answer.

Solution:
 the code uses a stack to perform an inorder traversal (left, root, right)
 and stops when the kth node is reached. 
 This leverages the BST’s property that nodes are visited in sorted order.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
    stack = []
    curr = root
    count = 0
    
    while curr or stack:
        # Push all left nodes onto the stack
        while curr:
            stack.append(curr)
            curr = curr.left
        
        # Process the top node
        curr = stack.pop()
        count += 1
        
        # If kth node is reached, return its value
        if count == k:
            return curr.val
        
        # Move to the right subtree
        curr = curr.right
    
    return -1  # Should never reach here given problem constraints

# Test Case 1
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
print(kthSmallest(root, 1))  # Output: 1

# Test Case 2
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
print(kthSmallest(root, 3))  # Output: 3