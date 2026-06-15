# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        help_list = []
        self.pre_process(root, help_list)
        pre = root
        root.left = None
        for i in range(1, len(help_list)):
            pre.right = help_list[i]
            help_list[i].left = None
            pre = help_list[i]
        return 
    
    def pre_process(self, root: Optional[TreeNode], help_list: List[TreeNode]):
        if not root:
            return 
        help_list.append(root)
        self.pre_process(root.left, help_list)
        self.pre_process(root.right, help_list)
        return 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        temp = root
        while temp:
            if temp.left:
                sub_left = temp.left
                while sub_left.right:
                    sub_left = sub_left.right
                sub_left.right = temp.right
                temp.right = temp.left
                temp.left = None
            temp = temp.right