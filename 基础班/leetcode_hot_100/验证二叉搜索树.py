# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        is_BST, root_max, root_min = self.process(root)
        return is_BST


    def process(self, root: Optional[TreeNode]):
        if root == None:
            return True, float('inf'), float('-inf')
        if not root.left and not root.right:
            return True, root.val, root.val # 是不是二叉搜索树， 最大值 最小值
        left_bool, left_max, left_min = self.process(root.left)
        right_bool, right_max, right_min = self.process(root.right)
        return left_max < root.val and right_min > root.val and left_bool and right_bool, max(left_max, right_max, root.val), min(left_min, right_min, root.val)

