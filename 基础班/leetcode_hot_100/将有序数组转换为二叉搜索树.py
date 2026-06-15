# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if len(nums) == 0:
            return None
        return self.process(nums, 0, len(nums)-1)

    def process(self, nums: List[int], left: int, right: int):
        if left > right:
            return None
        if left == right:
            new_node = TreeNode(nums[left])
            return new_node
        mid = (left + right) / 2
        new_node = TreeNode(nums[mid])
        new_node.left = self.process(nums, left, mid-1)
        new_node.right = self.process(nums, mid+1, right)
        return new_node