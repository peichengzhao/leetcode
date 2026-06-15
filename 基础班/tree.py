class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_pre_order(head: Node):
    if head == None:
        return 
    print(head.value)
    print_pre_order(head.left)
    print_pre_order(head.right)
    return

def print_in_order(head: Node):
    if head == None:
        return 
    print_in_order(head.left)
    print(head.value)
    print_in_order(head.right)
    return

def print_post_order(head: Node):
    if head == None:
        return 
    print_post_order(head.left)
    print_post_order(head.right)
    print(head.value)
    return


def pre_order_unrecursive(head: Node):
    if head == None:
        return 
    stack = []
    stack.append(head)
    cur = head
    while stack:
        cur = stack.pop()
        print(cur.value)
        if cur.right != None:
            stack.append(cur.right)
        if cur.left != None:
            stack.append(cur.left) 
    return

def post_order_unrecursive(head: Node):
    if head == None:
        return 
    stack = []
    result_stack = []
    stack.append(head)
    while stack:
        cur = stack.pop()
        result_stack.append(cur)
        if cur.left != None:
            stack.append(cur.left)
        if cur.right != None:
            stack.append(cur.right)
        result_stack.append(cur)
    while result_stack:
        print(result_stack.pop().value)
    return

def in_order_unrecursive(head: Node):
    if head == None:
        return
    stack = []
    while stack or head != None:
        if head != None:
            stack.append(head)
            head = head.left
        else:
            cur = stack.pop()
            print(cur.value)
            head = cur.right
    return

def level_order(head: Node):
    if head == None:
        return
    queue = []
    queue.append(head)
    while queue:
        cur = queue.pop(0)
        print(cur.value)
        if cur.left != None:
            queue.append(cur.left)
        if cur.right != None:
            queue.append(cur.right)
    return

from collections import deque
def fing_max_width(head: Node):
    if head == None:
        return 0
    head_map = {}
    head_map[head] = 1
    cur_level = 1
    cur_level_width = 0
    max_width = 0
    queue = deque()
    queue.append(head)
    while queue:
        cur = queue.popleft()
        cur_node_level = head_map[cur]
        if cur_node_level > cur_level:
            cur_level = cur_node_level
            cur_level_width = 1
        if cur_node_level == cur_level:
            cur_level_width += 1
        if cur.left != None:
            queue.append(cur.left)
            head_map[cur.left] = cur_node_level + 1
        if cur.right != None:
            queue.append(cur.right)
            head_map[cur.right] = cur_node_level + 1
        max_width = max(max_width, cur_level_width)
    return max_width




