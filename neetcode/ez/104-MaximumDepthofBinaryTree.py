# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Problem:
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_depth = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if depth > max_depth:
                max_depth = depth
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return max_depth

        # left_depth = self.maxDepth(root.left)
        # right_depth = self.maxDepth(root.right)

        # return 1 + max(left_depth, right_depth)