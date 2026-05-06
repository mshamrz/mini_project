from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.first_parent = None
        self.second_parent = None
        self.first_level = -1
        self.second_level = -1
        self.preorder(root, 0, None, x, y)

        return self.first_parent != self.second_parent and self.first_level == self.second_level

    def preorder(self, node, level, parent, x, y):
        if node:
            if node.val == x:
                self.first_parent = parent
                self.first_level = level
            if node.val == y:
                self.second_parent = parent
                self.second_level = level
            if node.left:
                self.preorder(node.left, level+1, node, x, y)
            if node.right:
                self.preorder(node.right, level + 1, node, x, y)
