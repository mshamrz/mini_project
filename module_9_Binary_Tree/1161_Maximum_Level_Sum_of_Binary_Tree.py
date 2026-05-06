from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        max_sum = float('-inf')
        best_level = 1
        level = 1
        while queue:
            current_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                current_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if current_sum > max_sum:
                max_sum = current_sum
                best_level = level
            level += 1
        return best_level
