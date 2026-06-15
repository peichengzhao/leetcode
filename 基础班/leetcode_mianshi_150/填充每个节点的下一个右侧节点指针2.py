class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque()
        if not root: return root
        queue.append((root, 0))
        pre_node = None
        pre_level = 0
        while queue:
            temp_node, temp_level = queue.popleft()
            if temp_level == pre_level and temp_node != root:
                pre_node.next = temp_node
            pre_node, pre_level = temp_node, temp_level
            if temp_node.left:
                queue.append((temp_node.left, temp_level+1))
            if temp_node.right:
                queue.append((temp_node.right, temp_level+1))
        return 



