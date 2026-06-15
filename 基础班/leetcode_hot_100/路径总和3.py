# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0
        def process(path: int, node: Optional[TreeNode]):
            nonlocal result
            if node == None:
                return 
            path += node.val
            if path == targetSum:
                result += 1
            process(path, node.left)
            process(path, node.right)
        process(0, root)
        def start(node: Optional[TreeNode]):
            if node == None:
                return 
            process(0, node)
            start(node.left)
            start(node.right)
        start(root)
        return result


###外层：选起点
# 内层：向下求和

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0
        def process(path: int, node: Optional[TreeNode]):
            nonlocal result
            if node == None:
                return 
            path += node.val
            if path == targetSum:
                result += 1
            process(0, node.left)
            process(0, node.right)
            process(path, node.left)
            process(path, node.right)
        process(0, root)
        return result