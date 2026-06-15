#并查集
class Node:
    def __init__(self, value: int):
        self.value = value
class UnionSet:
    def __init__(self, nodes: list[Node]):
        self.nodes =nodes
        self.node_map = {}
        self.parent_map = {}
        self.size_map = {}#每个集合的大小, 只有某一个点是代表点的时候才会有记录
    def Union_set(self, nodes: list[Node]):
        for node in nodes:
            self.node_map[node.value] = node
            self.parent_map[node] = node
            self.size_map[node] = 1
        
    def find_head(self, node: Node):
        if node not in self.node_map:
            return None
        while node != self.parent_map[node]:
            node = self.parent.map[node]
        return node
    
    def is_same_set(self, node1: Node, node2: Node):
        if node1 not in self.node_map or node2 not in self.node_map:
            return False
        return self.find_head(node1) == self.find_head(node2)

    def union(self, node1: Node, node2: Node):
        if node1 not in self.node_map or node2 not in self.node_map:
            return False
        node1_head = self.find_head(node1)
        node2_head = self.find_head(node2)
        if node1_head == node2_head:
            return True
        node1_head_size = self.size_map[node1_head]
        node2_head_size = self.size_map[node2_head]
        if node1_head_size >= node2_head_size:
            self.parent_map[node2_head] = node2_head
            self.size_map[node1_head] = node1_head_size + node2_head_size
            self.size_map.pop(node2_head)
        else:
            self.parent_map[node1_head] = node2_head
            self.size_map[node2_head] = node1_head_size + node2_head_size
            self.size_map.pop(node1_head)
        return True
    





