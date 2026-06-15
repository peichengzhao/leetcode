# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def mid_process(node: Optional[TreeNode]):
            nonlocal result
            if node == None:
                return 
            mid_process(node.left)
            result.append(node.val)
            mid_process(node.right)
            return 
        mid_process(root)
        return result[k-1]