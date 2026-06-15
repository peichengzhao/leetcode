# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from asyncio import FastChildWatcher
from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.check(root.left, root.right)
    
    def check(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        if left is None and right is not None:
            return False
        if left is not None and right is None:
            return False
        if left.val != right.val:
            return False
        return self.check(left.left, right.right) and self.check(left.right, right.left)





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if root.left and not root.right:
            return False
        elif not root.left and root.right:
            return False
        elif not root.left and not root.right:
            return True
        left_node = root.left
        right_node = root.right
        return self.judge(left_node, right_node)
    


    def judge(self, left: Optional[TreeNode], right:Optional[TreeNode]):
        if not left and not right:
            return True
        elif not left and right:
            return False
        elif left and not right:
            return False
        elif left.val != right.val:
            return False
        return self.judge(left.left, right.right) and self.judge(left.right, right.left)
        