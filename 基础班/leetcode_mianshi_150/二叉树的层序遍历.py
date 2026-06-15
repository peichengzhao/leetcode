# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if not root:
            return []
        res = []
        pre_level = -1
        temp = []
        queue.append((root, 0))
        while queue:
            pop_node, pop_level = queue.popleft()
            if pop_level > pre_level:
                res.append(temp)
                temp = []
                pre_level = pop_level
            temp.append(pop_node.val)
            if pop_node.left: queue.append((pop_node.left, pop_level+1))
            if pop_node.right: queue.append((pop_node.right, pop_level+1))
        res.append(temp)
        return res[1:]

