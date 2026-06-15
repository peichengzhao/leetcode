# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
from collections import deque
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if root is None:
#             return []
#         level = 1
#         results = []
#         queue = deque()
#         queue.append(root)
#         hash_map = {}
#         hash_map[root] = 1
#         temp = []
#         temp.append(root.val)
#         while queue:
#             cur = queue.popleft()
#             cur_level = hash_map[cur]
#             if cur_level == level:
#                 if cur != root:
#                     temp.append(cur.val)
#             else:
#                 results.append(temp)
#                 temp = []
#                 temp.append(cur.val)
#                 level += 1
#             if cur.left:
#                 queue.append(cur.left)
#                 hash_map[cur.left] = cur_level + 1
#             if cur.right:
#                 queue.append(cur.right)
#                 hash_map[cur.right] = cur_level + 1
#         results.append(temp)
#         return results

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        results = []
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            temp = []
            while size > 0:
                cur = queue.popleft()
                temp.append(cur.val)
                size -= 1
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            results.append(temp)
        return results

        











# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        my_deque = deque()
        size = 1
        my_deque.append(root)
        while my_deque:
            level_size = len(my_deque)
            level_list = []
            for i in range(level_size):
                node = my_deque.popleft()
                level_list.append(node.val)
                if node.left:
                    my_deque.append(node.left)
                if node.right:
                    my_deque.append(node.right)
            result.append(level_list)
        return result
            




# 





















