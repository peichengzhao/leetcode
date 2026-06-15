# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def process(path: int, node: Optional[TreeNode]):
            path += node.val
            if not node.left and not node.right:
                return True if path == targetSum else False
            left_result, right_result = False, False
            if node.left:
                left_result = process(path, node.left)
            if node.right:
                right_result = process(path, node.right)
            return left_result or right_result
        return process(0, root)