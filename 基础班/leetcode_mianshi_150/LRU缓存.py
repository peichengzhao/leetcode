class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.hash_map = {}
    
    def move_node_to_tail(self, node: Node):
        if node.next == self.tail:
            return 
        pre_node = node.pre
        next_node = node.next
        pre_node.next = next_node
        next_node.pre = pre_node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node

    def remove_head_next_node(self):
        if self.head.next == self.tail:
            return None

        tar_node = self.head.next
        self.head.next = tar_node.next
        tar_node.next.pre = self.head
        if self.head.next == self.tail:
            self.tail.pre = self.head
        

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        self.move_node_to_tail(self.hash_map[key])
        return self.hash_map[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].value = value
            self.move_node_to_tail(self.hash_map[key])
        else:
            if self.count == self.capacity:
                self.hash_map.pop(self.head.next.key)
                self.remove_head_next_node()
                self.count -= 1
            new_node = Node(key, value)
            self.tail.pre.next = new_node
            new_node.pre = self.tail.pre
            new_node.next = self.tail
            self.hash_map[key] = new_node
            self.count += 1



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)