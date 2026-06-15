from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class BSTIterator(object):

    def __init__(self, root):
        self.queue = deque()
        self.inOrder(root)
    
    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        self.queue.append(root.val)
        self.inOrder(root.right)

    def next(self):
        return self.queue.popleft()


    def hasNext(self):
        return len(self.queue) > 0
