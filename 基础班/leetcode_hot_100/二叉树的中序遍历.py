# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from unittest import result
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        self.process(root,result)
        return result
    
    def process(self, root: TreeNode, result: list[int]):
        if root is None:
            return
        self.process(root.left,result)
        result.append(root.val)
        self.process(root.right,result)
        return 






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []
        result = []
        self.pre_process(root, result)
        return result
        
    def pre_process(self, root: Optional[TreeNode], result: List[int]):
        if root == None:
            return 
        self.pre_process(root.left, result)
        result.append(root.val)
        self.pre_process(root.right, result)