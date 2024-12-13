# Link: https://leetcode.com/problems/invert-binary-tree/
# Problem:
# Given the root of a binary tree, invert the tree, and return its root.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

    def invertTreeDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

    def invertTreeBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

# Helper function to print the tree in level order
def printLevelOrder(root):
    if not root:
        return "Empty Tree"
    
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append("None")
    
    return result

# Example Binary Tree
#       1
#      / \
#     2   3
#    / \
#   4   5    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Original Tree Level Order:", printLevelOrder(root))

check = Solution()
invertTree = check.invertTree(root)

# Test DFS Inversion
invertedRootDFS = check.invertTreeDFS(root)
print("Inverted Tree Level Order (DFS):", printLevelOrder(invertedRootDFS))

# Recreate the original tree for BFS test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Test BFS Inversion
invertedRootBFS = check.invertTreeBFS(root)
print("Inverted Tree Level Order (BFS):", printLevelOrder(invertedRootBFS))