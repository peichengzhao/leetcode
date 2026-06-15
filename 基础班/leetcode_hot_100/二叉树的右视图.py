# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
# 利用层序遍历 先写一个版本

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        from typing import Deque
        deque = Deque()
        deque.append([root, 1])
        pre = TreeNode(0)
        pre_level = 0
        temp = 0
        while deque:
            pop_node, pop_level = deque.popleft()
            if pop_level > pre_level:
                result.append(pre.val)
            pre = pop_node
            pre_level = pop_level
            if pop_node.left:
                deque.append([pop_node.left, pop_level+1])
            if pop_node.right:
                deque.append([pop_node.right, pop_level+1])
        result.append(pre.val)
        return result[1:]