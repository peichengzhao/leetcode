from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def process(root: Optional[TreeNode]):
            if root == None:
                return 0
            left_depth = process(root.left)
            right_depth = process(root.right)
            return max(left_depth, right_depth) + 1
        return process(root)
            
            