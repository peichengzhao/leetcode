# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        pre = 1
        pre_node = root
        if not root:
            return []
        result = []
        result.append()
        # deque = queue((root, 1))
        queue = deque([(root,1)])

        while queue:
            node, level = queue.popleft()
            if level > pre:
                pre = level
                result.append(pre_node.val)
            pre_node = node
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        result.append(pre_node.val)
        return result
