# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

from 暴力递归到动态规划4 import process
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth, diameter = self.process(root)
        return diameter
    def process(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0, 0 #返回最大深度和直径
        left_depth, left_diameter = self.process(root.left)
        right_depth, right_diameter = self.process(root.right)
        depth = max(left_depth, right_depth) + 1
        diameter = max(left_diameter, right_diameter, left_depth + right_depth)
        return depth, diameter










# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth, diameter = self.process(root)
        return diameter
    
    def process(self, root: Optional[TreeNode], depth: int, diameter: int):
        if root is None:
            return 0, 0 
        left_depth, left_diameter = self.process(root.left)
        right_depth, right_diameter = self.process(root.right)
        depth = max(left_depth, right_depth) + 1
        diameter = max(left_depth + right_depth, right_diameter, left_diameter)
        return depth, diameter
        























