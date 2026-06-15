class ListNode:
    # 错误1修复：必须存 key
    def __init__(self, key, value) -> None:
        self.pre = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.pre, self.head.next = None, self.tail
        self.tail.pre, self.tail.next = self.head, None
        self.hash_map = {}

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        self.move_node_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            self.move_node_to_head(node)  # 错误2修复
            return
        
        new_node = ListNode(key, value)
        self.hash_map[key] = new_node

        # 插入头部
        new_node.next = self.head.next
        self.head.next.pre = new_node
        self.head.next = new_node
        new_node.pre = self.head  # 补全指针

        self.size += 1

        if self.size > self.capacity:
            self.remove_tail_node()

    def move_node_to_head(self, node: ListNode):
        # 摘除
        node.pre.next = node.next
        node.next.pre = node.pre

        # 插入头部
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node  # 错误4修复
        self.head.next = node

    def remove_tail_node(self):
        tail_node = self.tail.pre  # 拿到真正的尾节点
        if tail_node == self.head:
            return
        
        # 错误3修复：删除 hash map 中的 key
        self.hash_map.pop(tail_node.key)

        # 移除节点
        tail_node.pre.next = self.tail
        self.tail.pre = tail_node.pre

        self.size -= 1
        return 
        