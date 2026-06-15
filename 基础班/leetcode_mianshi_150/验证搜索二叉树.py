# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def vaild_process(node: Optional[TreeNode]):
            cur_val = node.val
            cur_max = cur_val
            cur_min = cur_val
            cur_result = True
            if node.left:
                left_valid, left_max, left_min = vaild_process(node.left)
                cur_max = max(cur_max, left_max)
                cur_min = min(cur_min, left_min)
            if node.right:
                right_valid, right_max, right_min = vaild_process(node.right)
                cur_max = max(cur_max, right_max)
                cur_min = min(cur_min, right_min)
            if node.left and left_max >= cur_val:
                cur_result = False
            if node.right and right_min <= cur_val:
                cur_result = False
            if (node.left and not left_valid) or (node.right and not right_valid):
                cur_result = False
            return cur_result, cur_max, cur_min
        result, result_max ,result_min = vaild_process(root)
        return result





class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def vaild_process(node: Optional[TreeNode]):
            if not node:
                return True, float("-inf"), float("inf")
            left_valid, left_max, left_min = vaild_process(node.left)
            right_valid, right_max, right_min = vaild_process(node.right)
            return left_valid and right_valid and (node.val > left_max) and (node.val<right_min), max(node.val, left_max, right_max), min(node.val, left_min, right_min)
        return vaild_process(root)[0]