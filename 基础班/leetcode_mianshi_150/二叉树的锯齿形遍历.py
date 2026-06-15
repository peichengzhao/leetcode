# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 1)])
        temp = [root.val]
        reverse = True
        result = []
        pre = 0
        while queue:
            node, level = queue.popleft()
            if level > pre:
                if reverse:
                    result.append(temp[::-1])
                    reverse = False
                else:
                    result.append(temp)
                    reverse = True
                temp = []
                pre = level
            temp.append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        result.append(temp[::-1] if reverse else temp)
        return result
