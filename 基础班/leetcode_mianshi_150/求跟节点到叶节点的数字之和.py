# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        def process(node: Optional[TreeNode], path: int):
            nonlocal result
            if node == None:
                return
            path = path * 10 + node.val
            if not node.left and not node.right:
                result += path
            process(node.left, path)
            process(node.right, path)
            return 
        process(root, 0)
        return result
            
