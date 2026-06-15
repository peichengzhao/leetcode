# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.process(root, 0)
    

    def process(self, root: TreeNode, depth: int):
        if root is None:
            return 0
        left_depth = self.process(root.left, depth)
        right_depth = self.process(root.right, depth)
        return max(left_depth, right_depth) + 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.depth_process(root)
    
    def depth_process(self, root: Optional[TreeNode]):
        if root == None:
            return 0
        #左高度
        left_depth = self.depth_process(root.left)
        right_depth = self.depth_process(root.right)
        return max(left_depth, right_depth) + 1
















