# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1
        help_list = []
        self.mid_process(root, help_list)
        return help_list[k-1]
    
    def mid_process(self, root: Optional[TreeNode], help_list: List[int]):
        if root is None:
            return 
        self.mid_process(root.left, help_list)
        help_list.append(root.val)
        self.mid_process(root.right, help_list)