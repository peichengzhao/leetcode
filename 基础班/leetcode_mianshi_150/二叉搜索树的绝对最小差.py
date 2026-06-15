from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        temp = []
        def mid_process(node: Optional[TreeNode]):
            nonlocal temp
            if node == None:
                return
            mid_process(node.left)
            temp.append(node.val)
            mid_process(node.right)
            return 
        mid_process(root)
        min_value = float("inf")
        for i in range(1, len(temp)):
            min_value = min(min_value, abs(temp[i] - temp[i-1]))
        return min_value            