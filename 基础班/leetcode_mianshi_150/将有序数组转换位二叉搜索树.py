# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums or len(nums) == 0:
            return None
        def process(left: int, right: int):
            nonlocal nums
            if left == right:
                return TreeNode(nums[left])
            elif left > right:
                return None
            else:
                mid = (left + right) // 2
                mid_node = TreeNode(nums[mid])
                mid_node.left = process(left, mid-1)
                mid_node.right = process(mid+1, right)
                return mid_node
        return process(0, len(nums)-1)