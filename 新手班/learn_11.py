# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def hasPathSum(self, root, targetSum):
#         """
#         :type root: Optional[TreeNode]
#         :type targetSum: int
#         :rtype: bool
#         """
#         if (root is None):
#             return False
#         is_sum = False
#         is_sum = self.is_path_sum(root, pre_sum=0, sum=targetSum)
#         return is_sum
#     def is_path_sum(self, root, pre_sum, sum):
#         if (root.left is None and root.right is None): # 叶子节点
#             if pre_sum + root.val == sum:
#                 return True
#         # 不是叶子节点
#         presum += root.val
#         if(root.left is not None):
#             self.is_path_sum(root.left, pre_sum, sum)
#         if(root.right is not None):
#             self.is_path_sum(root.right, pre_sum, sum)
#         return False


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.result = []
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        path = []
        self.result = self.is_path_sum(root, [], targetSum)
        return self.result

    def is_path_sum(self, root, path,targetSum):
        path.append(root.val)
        if (root.left is None and root.right is None):
            if sum(path) == targetSum:
                self.result.append(path.copy())
        if (root.left is not None):
            self.is_path_sum(root.left, path, targetSum)
        if (root.right is not None):
            self.is_path_sum(root.right, path, targetSum)
        path.pop() 
        return self.result