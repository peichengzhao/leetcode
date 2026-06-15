# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        self.reverse(root)
        return root
    def reverse(self, root: TreeNode):
        if root is None:
            return 
        left_node = root.left
        right_node = root.right
        root.left = right_node        
        root.right = left_node
        self.reverse(root.left)
        self.reverse(root.right)
        return



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.process(root)
        return root


    def process(self, root: Optional[TreeNode]):
        if root is None:
            return None
        # 反转左边
        temp = root.right
        root.right = root.left
        root.left = temp
        self.process(root.left)
        #反转右边
        self.process(root.right)