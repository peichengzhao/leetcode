from typing import Optional

# 题目定义的Node类（无需修改）
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next  # 指向下一个节点（原/新链表节点）
        self.random = random  # 随机指针（指向任意节点或None）

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # 边界条件：空链表直接返回None
        if not head:
            return None
        
        # 哈希表：键=原链表节点，值=对应的新拷贝节点（深拷贝核心：新节点和原节点完全独立）
        old_to_new = {}
        
        # 第一步：遍历原链表，创建所有新节点，仅初始化val，存入哈希表
        current = head
        while current:
            # 每个新节点都是全新创建的，满足“深拷贝”要求
            old_to_new[current] = Node(current.val)
            current = current.next
        
        # 第二步：遍历原链表，设置新节点的next和random指针（只指向新节点）
        current = head
        while current:
            # 新节点的next = 原节点next对应的新节点（若原next为None，get返回None）
            old_to_new[current].next = old_to_new.get(current.next)
            # 新节点的random = 原节点random对应的新节点（若原random为None，get返回None）
            old_to_new[current].random = old_to_new.get(current.random)
            current = current.next
        
        # 返回复制链表的头节点（原头节点对应的新节点）
        return old_to_new[head]