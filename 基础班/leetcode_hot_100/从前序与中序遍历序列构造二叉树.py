# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def process(pre_begin: int, pre_end: int, in_begin: int, in_end: int):
            if pre_begin > pre_end:
                return None
            if pre_begin == pre_end:
                return TreeNode(preorder[pre_begin])
            head = TreeNode(preorder[pre_begin])
            temp = in_begin
            while inorder[temp] != preorder[pre_begin] and temp <= in_end:
                temp += 1
            head.left = process(pre_begin=pre_begin+1, pre_end=pre_begin + temp-in_begin, in_begin=in_begin, in_end = temp-1)
            head.right = process(pre_begin=pre_begin + temp-in_begin+1, pre_end=pre_end, in_begin=temp+1, in_end=in_end)
            return head
        head = process(0, len(preorder)-1, 0, len(inorder)-1)
        return head