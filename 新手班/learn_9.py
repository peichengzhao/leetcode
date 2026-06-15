# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        temp_queue = []
        temp_queue.append(root)
        while temp_queue:
            temp_list = []
            temp_length = len(temp_queue)
            for i in range(temp_length):
                temp_node = temp_queue.pop(0)
                temp_list.append(temp_node.val)
                if temp_node.left is not None:
                    temp_queue.append(temp_node.left)
                if temp_node.right is not None:
                    temp_queue.append(temp_node.right)
            result.append(temp_list)
        return result[::-1]




        