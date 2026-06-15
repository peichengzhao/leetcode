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
        temp_list = []
        def pre_proess(node: Optional[TreeNode]):
            nonlocal temp_list
            if node == None:
                return 
            temp_list.append(node)
            pre_proess(node.left)
            pre_proess(node.right)
            return
        pre_proess(root)
        pre = None
        for i in range(len(temp_list)-1, -1, -1):
            temp_list[i].left = None
            temp_list[i].right = pre
            pre = temp_list[i]
        return root


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
        return 














