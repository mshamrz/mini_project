from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_index = 0
        self.inorder_map = {}
        for i in range(len(inorder)):
            self.inorder_map[inorder[i]] = i
        return self.build_tree_helper(preorder, inorder, 0, len(inorder) - 1)

    def build_tree_helper(self, preorder, inorder, inorder_start, inorder_end):
        if inorder_start > inorder_end:
            return None
        root_value = preorder[self.preorder_index]
        root = TreeNode(root_value)
        root_index = self.inorder_map[root_value]
        self.preorder_index += 1
        root.left = self.build_tree_helper(preorder, inorder, inorder_start, root_index - 1)
        root.right = self.build_tree_helper(preorder, inorder, root_index + 1, inorder_end)
        return root
