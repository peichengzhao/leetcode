# Definition for a binary tree node.
from ast import NodeTransformer
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def find_index(left: int, right: int, number: int):
            for i in range(left, right+1):
                if inorder[i] == number:
                    return i
        def process(pre_left: int, pre_right: int, inorder_left: int, inorder_right: int):
            if pre_left > pre_right or inorder_left > inorder_right:
                return None
            if pre_left == pre_right:
                return TreeNode(preorder[pre_left])
            root = TreeNode(preorder[pre_left])
            index = find_index(inorder_left, inorder_right, preorder[pre_left])
            root.left = process(pre_left+1, index-inorder_left+pre_left, inorder_left, index-1)
            root.right = process(index-inorder_left+pre_left+1, pre_right, index+1, inorder_right)
            return root
        length = len(preorder)
        return process(0 , length-1, 0, length-1)





class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        