# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None
        temp = False
        def process(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode',):
            nonlocal result, temp
            if not root:
                return False, False
            have_p, have_q = False, False
            if root == p:
                have_p = True
            if root == q:
                have_q = True
            left_have_p, left_have_q = process(root.left, p, q,)
            right_have_p, right_have_q = process(root.right, p,q)
            res_have_p, res_have_q = have_p or left_have_p or right_have_p, have_q or left_have_q or right_have_q
            if res_have_p and res_have_q and not temp:
                temp = True
                result = root
            return res_have_p, res_have_q
        process(root, p, q)
        return result

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right: #p, q 分别在两个节点上
            return root
        return left if left else right


















class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right






