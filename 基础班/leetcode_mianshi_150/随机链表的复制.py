"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import List, Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
from typing import Optional

# 题目定义的Node类（无需修改）
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = None  # 指向下一个节点（原/新链表节点）
        self.random = None  # 随机指针（指向任意节点或None）

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head or head == None:
            return None
        # 哈希表：键=原链表节点，值=对应的新拷贝节点（深拷贝核心：新节点和原节点完全独立）
        old_to_new = {}
        temp = head
        pre = Node(0)
        while temp:
            new_node = Node(temp.val)
            pre.next = new_node
            pre = new_node
            old_to_new[temp] = new_node
            temp = temp.next
        temp = head
        while temp:
            if temp.random:
                old_to_new[temp].random = old_to_new[temp.random]
            temp = temp.next
        return old_to_new[head]