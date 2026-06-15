# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def process(node: Optional[TreeNode]):
            #返回高度
            if not node:
                return 0
            return max(process(node.right), process(node.left)) + 1
        def process_2(node: Optional[TreeNode]):
            if not node:
                return 0
            left_level, right_level = process(node.left), process(node.right)
            if left_level == right_level:
                return 2**(left_level) + process_2(node.right)
            else:
                return 2**(right_level) + process_2(node.left)
        return process_2(root)
