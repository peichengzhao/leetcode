# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def process(node: Optional[TreeNode]):
            if node == None:
                return None
            node_left = process(node.left)
            node_right = process(node.right)
            node.left, node.right = node_right, node.left
            return node
        return process(root)

