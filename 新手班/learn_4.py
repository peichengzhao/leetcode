from ast import NodeTransformer, Nonlocal


class Node:
    """单向链表节点类（修正版）"""
    def __init__(self, value: int = 0):
        self.value = value  # 数据域
        self.next = None    # 指针域：初始化为None，避免递归

class LinkList:
    """单向链表类（带尾指针优化，支持反转）"""
    def __init__(self):
        self.head = None    # 头节点：空链表时为None
        self.tail = None    # 尾节点：空链表时为None
        self.length = 0     # 链表长度

    def add(self, value: int):
        """尾插法添加节点（O(1)）"""
        new_node = Node(value)
        if self.head is None:  # 空链表：头/尾都指向新节点
            self.head = new_node
            self.tail = new_node
        else:  # 非空链表：尾节点next指向新节点，更新尾指针
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def traverse(self):
        """遍历链表，返回所有节点值的列表"""
        res = []
        cur = self.head
        while cur:
            res.append(cur.value)
            cur = cur.next
        return res

    def fanzhuan(self):
        """反转单向链表（核心逻辑）"""
        if self.head is None or self.head.next is None:
            return  # 空链表或只有一个节点，无需反转
        
        pre = None  # 前驱节点：初始为None
        cur = self.head  # 当前节点：从头节点开始
        self.tail = self.head  # 反转后原头节点变为尾节点
        while cur:
            next_node = cur.next  # 1. 保存当前节点的下一个节点（避免断链）
            cur.next = pre        # 2. 反转当前节点的指针（指向前驱）
            pre = cur             # 3. 前驱节点后移（变为当前节点）
            cur = next_node       # 4. 当前节点后移（变为之前保存的next）
        self.head = pre  # 反转后，pre指向最后一个节点，作为新头节点



#使用单链表实现队列和栈
class Node:
    def __init__(self, value:int):
        self.value = value
        self.next = None
class Myqueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def init(self):
        self.head = None
        self.tail = None
        self.head.next = self.tail
        self.length = 0

    def add(self, value: int):
        new_node = Node(value)
        self.length += 1 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def pop(self):
        if self.head is None:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            self.length -= 1
            return value

#两个链表的合并 给定两个有序的链表，合并成一个有序的链表
def merge_linklist(linklist1: LinkList, linklist2: LinkList):
    if linklist1 is None or linklist2 is None:
        return None
    temp = None
    result = LinkList()
    while linklist1 is not None and linklist2 is not None:
        if linklist1.value < linklist2.value:
            temp = linklist1
            linklist1 = linklist1.next
            result.add(temp.value)
        else:
            temp = linklist2
            linklist2 = linklist2.next
            result.add(temp.value)
    while linklist1 is not None:
        temp = linklist1
        linklist1 = linklist1.next
        result.add(temp.value)
    while linklist2 is not None:
        temp = linklist2
        linklist2 = linklist2.next
        result.add(temp.value)
    return result







