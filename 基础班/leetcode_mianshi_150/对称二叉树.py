# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def process(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if not node1 and not node2:
                return True
            if (not node1 and node2) or (not node2 and node1):
                return False
            if node1.val != node2.val:
                return False
            return process(node1.left, node2.right) and process(node1.right, node2.left)
        
        return process(root.left, root.right)
             