# 判断是否是平衡二叉树



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        
        height, balance = self.is_balance_tree(root)
        return balance

    def is_balance_tree(self, root):
        if root is None:
            return 0, True # 返回高度和是否平衡
        if root.left is None and root.right is None:
            return 1, True
        left_height, left_balance = self.is_balance_tree(root.left)
        right_height, right_balance = self.is_balance_tree(root.right)
        if not left_balance or not right_balance:
            return 0, False
        if abs(left_height - right_height) > 1 :
            return 0, False
        return max(left_height, right_height) + 1 , True







# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        valid, min_value, max_value = self.is_valid_bst(root)
        return valid
    def is_valid_bst(self, root):
        if root is None:
            return True
        min_value = root.val
        max_value = root.val
        left_valid, left_min, left_max = self.is_valid_bst(root.left)
        right_valid, right_min, right_max = self.is_valid_bst(root.right)
        if left_valid is not None:
            min_value = min(left_min, min_value)
            max_value = max(left_max, max_value)
        if right_valid is not None:
            min_value = min(right_min, min_value)
            max_value = max(right_max, max_value)
        valid = True
        if left_valid is not None:
            valid = root.val > left_max
        if right_valid is not None and valid == True:
            valid = root.val < right_min
        if left_valid is False or right_valid is False:
            valid = False
        return valid, min_value, max_value



        