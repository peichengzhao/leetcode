#Dijkstra算法

from typing import List
from collections import deque

# 图   有向图  无向图
#邻接表 和 邻接矩阵
# 最大值
max_num = float('inf')


class Node:
    def __init__(self, value: int):
        self.value = value  #编号
        self.in_num = 0
        self.out_num = 0
        self.nexts = [] # 指向的节点
        self.edges = [] # 出去的边

class Edge:
    def __init__(self, weight: int, from_node: Node, to_node: Node):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
    def get_number_of_nodes(self):
        return len(self.nodes)

    def union_graph(self, matrix: list[list[int]]):
        graph = Graph()
        for i in range(len(matrix)):
            weight = matrix[i][0]
            from_node = matrix[i][1]
            to_node = matrix[i][2]
            if from_node not in graph.nodes:
                graph.nodes[from_node] = Node(from_node)
            if to_node not in graph.nodes:
                graph.nodes[to_node] = Node(to_node)
            from_node_obj = graph.nodes[from_node]
            from_node_obj.nexts.append(to_node_obj)
            from_node_obj.edges.append(new_edge)
            to_node_obj = graph.nodes[to_node]
            from_node_obj.out_num += 1
            to_node_obj.in_num += 1
            new_edge = Edge(weight=weight, from_node=from_node_obj, to_node=to_node_obj)
            graph.edges[new_edge] = new_edge            
        return graph
    
    def wfs(self, start_node: Node):
        if start_node is None:
            return
        hash_set = {}
        from collections import deque
        from typing import List # 刷题
        help_queue = deque()
        help_queue.append(start_node)
        hash_set[start_node] = True
        while help_queue:
            cur = help_queue.popleft()
            print(cur.value)
            for next in cur.nexts:
                if next not in hash_set:
                    help_queue.append(next)
                    hash_set[next] = True
        return 
    def dfs(self, start_node: Node):
        if start_node is None:
            return
        help_stack = []
        help_set = {}
        help_stack.append(start_node)
        print(start_node.value)
        help_set[start_node] = True
        while help_stack:
            cur = help_stack.pop()
            for next in cur.nexts:
                if next not in help_set:
                    help_stack.append(cur)
                    help_stack.append(next)
                    print(next.value)
                    help_set[next] = True
                    break
        return 
# 拓扑排序
def topo_sort(graph: Graph):
    in_map = {} # key: node, value: in_num
    from collections import deque
    zero_in_queue = deque()
    for node in graph.nodes.values():
        in_map[node] = node.in_num
        if node.in_num == 0:
            zero_in_queue.append(node)
    result =[]
    while zero_in_queue:
        cur = zero_in_queue.popleft()
        result.append(cur)
        for next in cur.nexts:
            in_map[next] -= 1
            if in_map[next] == 0:
                zero_in_queue.append(next)
    return result
#Dijkstra算法
def dijkstra(graph: Graph, start_node: Node):
    if start_node is None:
        return None
    distance_map = {}
    distance_map[start_node] = 0
    selected_nodes = []
    selected_nodes.append(start_node)
    while len(selected_nodes) < graph.get_number_of_nodes():
        min_node, min_distance = get_min_distance_and_unselected_node(distance_map=distance_map, selected_nodes=selected_nodes)
        selected_nodes.append(min_node)
        for edge in min_node.edges:
            if edge.to_node in selected_nodes:
                continue
            to_node = edge.to_node
            if to_node not in distance_map:
                distance_map[to_node] = min_distance + edge.weight
            else:
                distance_map[to_node] = min((min_distance + edge.weight), distance_map[to_node])
    return distance_map

def get_min_distance_and_unselected_node(distance_map: dict, selected_nodes: list):
    min_distance = float('inf')
    min_node = None
    for node, distance in distance_map.items():
        if node not in selected_nodes and distance <= min_distance:
            min_distance = distance
            min_node = node
    return min_node, min_distance




