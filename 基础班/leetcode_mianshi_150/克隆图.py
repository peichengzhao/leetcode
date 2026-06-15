from typing import List

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node or not node[0]:
            return node
        lookup = {}
        def bfs(node):
            if not node:
                return 
            clone = Node(node.val, [])
            lookup[node] = clone
            queue = deque()
            queue.append(node)
            while queue:
                temp = queue.popleft()
                for n in temp.neighbors:
                    if n not in lookup:
                        queue.append(n)
                        lookup[n] = Node(n.val, [])
                    lookup[temp].neighbors.append(lookup[n])
            return clone
        return bfs(node)