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

# 最小生成树 并查集解决此类问题最有效
# 小根堆



# 暴力递归
#examples

def computer(n:int):
    if n == 1:
        return 1
    else:
        return n * computer(n-1)

#汉诺塔问题
def LeftToRight(n: int):
    if n == 1:
        print("Move 1 from left to right")
        return 
    else:
        LeftToMiddle(n-1)
        print("Move 1 from left to right")
        MiddleToRight(n-1)
    
def LeftToMiddle(n: int):
    if n == 1:
        print("Move 1 from left to Middle")
        return 
    else:
        LeftToRight(n-1)
        print("Move 1 from left to Middle")
        RightToMiddle(n-1)

def MiddleToRight(n: int):
    if n == 1:
        print("Move 1 from Middle to right")
        return 
    else:
        MiddleToLeft(n-1)
        print("Move 1 from Middle to right")
        LeftToRight(n-1)
    
def MiddleToLeft(n: int):
    if n == 1:
        print("Move 1 from Middle to left")
        return 
    else:
        MiddleToRight(n-1)
        print("Move 1 from Middle to left")
        RightToLeft(n-1)
    
def RightToLeft(n: int):
    if n == 1:
        print("Move 1 from right to left")
        return  

def hanoi(n: int, from_stack, to_stack, other_stack):
    if n == 1:
        # 修复错误1：用变量n表示盘子编号，而非固定数字1
        print(f"Move {n} from {from_stack} to {to_stack}")
        return 
    # 修复错误2：第一个递归的入参顺序：from → other，借助 to
    hanoi(n-1, from_stack, other_stack, to_stack)
    # 移动第n个盘子（最大的那个），从原位置到目标位置
    print(f"Move {n} from {from_stack} to {to_stack}")
    # 第三个递归：other → to，借助 from （这行你原本写的是对的！）
    hanoi(n-1, other_stack, to_stack, from_stack)

# 测试调用：3个盘子，从A移到C，借助B中转


# 逆序一个栈 不使用额外空间


def get_and_remove_last(stack: list[int]):
    result = stack.pop()
    if len(stack) == 0:
        return result
    else:
        last = get_and_remove_last(stack)
        stack.append(result)
        return last

def reverse_stack(stack: list[int]):
    if len(stack) == 0:
        return 
    else:
        last = get_and_remove_last(stack)
        reverse_stack(stack)
        stack.append(last)
    return stack


def print_all_subsequences(str: str):
    process(str, 0, "")

def process(str: str, index: int, path: str):
    if index == len(str):
        print(path)
        return
    process(str, index+1, path)
    process(str, index+1, path + str[index])
    return
def print_all_permutations(str: str):
    for i in range(len(str)):
        for j in range(i, len(str)):
            print(str[i:j+1])
    return 


def print_all_permutations(str: str):
    results = []
    path = ""
    hash_set = {}
    process1(str, 0, path, results)
    return results

def process1(str: str, index: int, path: str, results: list[str], hash_set: dict):
    if index == len(str):
        results.append(path)
        hash_set[path] = True
        return  #出口
    path_1 = path + str[index]
    path_2 = path
    process1(str, index+1, path_1, results, hash_set)
    process1(str, index+1, path_2, results, hash_set)
    return




# A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8, I=9, J=10, K=11, L=12, M=13, N=14, O=15, P=16, Q=17, R=18, S=19, T=20, U=21, V=22, W=23, X=24, Y=25, Z=26
# 给定一个数字字符串，求有多少种字母组合方式
# 111 -> AAA, KA, AK

def find_all_ways(str: str):
    results = []



def process3(str: str, index:int, path:str, results:list[str]): # 0-index-1已经转化完毕
    if index == len(str):
        return 1
    if str[index] == '0':
        return 0
    elif str[index] == '1':
        res = process3(str, index+1, path, results)
        if index + 1 < len(str):
            res += process3(str, index+2, path, results)
        return res
    elif str[index] == '2':
        res = process3(str, index+1, path, results)
        if index + 1 < len(str) and str[index+1] <= '6':
            res += process3(str, index+2, path, results)
        return res
    else:
        return process3(str, index+1, path, results)
    return 


# 背包问题
def bag_problem(weights: list[int], values: list[int], bag: int):
    results = []
    max_value = process5(weights, values, 0, 0, 0, results, bag)
    return max_value

def process5(weights: list[int], values: list[int], index: int, already_weight: int, already_value: int, results: list[int], bag: int):
    if already_weight > bag:
        return -1 # 无效解
    if index == len(weights):
        return 0 # 方案有效
    p1 = process5(weights, values, index+1, already_weight, already_value, results, bag) # 不选当前物品
    p2 = process5(weights, values, index+1, already_weight+weights[index], already_value+values[index], results, bag) # 选当前物品
    return max(p1, p2)

def process6(weights: list[int], values: list[int], index: int, rest_weight: int):
    # 修复问题3：剩余承重不足，返回0（无收益），而不是-1
    if rest_weight <= 0:
        return 0
    # 递归终止条件：遍历完所有物品，无收益，返回0（你的代码这行完全正确）
    if index == len(weights):
        return 0
    
    # 分支1：不选第index个物品，直接去下一个物品，剩余承重不变
    pi = process6(weights, values, index+1, rest_weight)
    
    # 分支2：选第index个物品（新增超重校验+修复核心逻辑：累加价值）
    pi2 = 0 # 默认不选
    if weights[index] <= rest_weight: # 修复问题4：超重校验，能装下才选
        # 修复问题1：选当前物品，累加当前价值 + 后续递归的价值
        pi2 = values[index] + process6(weights, values, index+1, rest_weight - weights[index])
    
    # 两种选择取最大价值，返回最优解
    return max(pi, pi2)

#纸牌博弈
def card_game(cards: list[int]):
    xianshou_max = xianshou_process7(cards, 0, len(cards)-1)
    houshou_max = houshou_process7(cards, 0, len(cards)-1)
    return max(xianshou_max, houshou_max)


def xianshou_process7(cards: list[int], left: int, right: int):
    #如果我是先手,返回最好结果
    if left == right:
        return cards[left]
    select_left = cards[left] + houshou_process7(cards, left+1, right) # 先手选择左边的牌
    select_right = cards[right] + houshou_process7(cards, left, right-1)
    return max(select_left, select_right)

def houshou_process7(cards: list[int], left: int, right: int):
    if left == right:
        return 0
    select_left = xianshou_process7(cards, left+1, right) # 后手选择左边的牌
    select_right = xianshou_process7(cards, left, right-1) # 后手选择右边的牌
    return min(select_left, select_right)


























