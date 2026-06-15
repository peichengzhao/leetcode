# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def process(p1: Optional[TreeNode], q1: Optional[TreeNode]):
            if p1 == None and q1 == None:
                return True
            elif p1 != None and q1 == None:
                return False
            elif p1 == None and q1 != None:
                return False
            else:
                if p1.val != q1.val:
                    return False
                else:
                    left = process(p1.left, q1.left)
                    right = process(p1.right, q1.right)
                    return left and right
        return process(p, q)