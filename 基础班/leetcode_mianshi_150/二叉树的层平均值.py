# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        result = []
        pre_level = -1
        queue = deque()
        queue.append((root, 0))
        temp, count = 0, 0
        while queue:
            pop_node, pop_level = queue.popleft()
            if pop_level > pre_level:
                if count != 0:
                    result.append(temp / count)
                temp = pop_node.val
                count = 1
                pre_level = pop_level
            else:
                temp += pop_node.val
                count += 1
            if pop_node.left:
                queue.append((pop_node.left, pop_level + 1))
            if pop_node.right:
                queue.append((pop_node.right, pop_level+1))
        result.append(temp / count)
        return result