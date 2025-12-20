## leetcode


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


tree_node = Node(1)
tree_node.left = Node(2)
tree_node.right = Node(3)
tree_node.left.left = Node(4)
tree_node.left.right = Node(5)
tree_node.right.left = Node(6)
tree_node.right.right = Node(7)

#先序遍历
def print_node(node: Node):
    print(f"{node.value}",  end="  ")

def pre_order(tree_node: Node):
    if tree_node is None:
        return 
    print_node(tree_node)
    pre_order(tree_node.left)
    pre_order(tree_node.right)

def in_order(tree_node: Node):
    if tree_node is None:
        return 
    in_order(tree_node.left)
    print_node(tree_node)
    in_order(tree_node.right)

def post_order(tree_node: Node):
    if tree_node is None:
        return 
    post_order(tree_node.left)
    post_order(tree_node.right)
    print_node(tree_node)

# 判断Q是不是等于P

def judge_tree(p: Node, Q: Node):
    if p is None and Q is None:
        return True
    if p is None or Q is None:
        return False
    if p.value != Q.value:
        return False
    result_bool = judge_tree(p.left, Q.left) and judge_tree(p.right, Q.right)
    return result_bool

# 判断一棵树是否是镜面树
def judge_mirror_tree(tree_node_left: Node, tree_node_right: Node):
    if tree_node_left is None and tree_node_right is None:
        return True
    if tree_node_left is None or tree_node_right is None:
        return False
    if tree_node_left.value != tree_node_right.value:
        return False
    return tree_node_left.value == tree_node_right.value and judge_mirror_tree(tree_node_left.left, tree_node_right.right) and judge_mirror_tree(tree_node_left.right, tree_node_right.left)

# 返回一棵树的最大深度
def get_max_depth(tree_node: Node):
    if tree_node is None:
        return 0
    return max(get_max_depth(tree_node.left), get_max_depth(tree_node.right)) + 1 

# 根据先序遍历结果和后序遍历结果重建一棵树

def build_tree(pre_order: list, in_order: list):
    # pre_order = [1, 2, 4, 5, 3, 6, 7]
    # in_order = [4, 2, 5, 1, 6, 3, 7]
    if len(pre_order) == 0 or len(in_order) == 0:
        return None
    if len(pre_order) != len(in_order):
        return None
    return build_tree_helper(pre_order, 0, len(pre_order) - 1, in_order, 0, len(in_order) - 1)

# 有一棵树，知道先序遍历结果和后序遍历结果，重建一棵树
def build_tree_helper(pre_order: list, l1: int, r1: int, in_order: list, l2: int, r2: int):
    if l1 > r1:
        return None
    if l1 == r1:
        return Node(pre_order[l1])
    head_node = Node(pre_order[0])
    idx = in_order.index(pre_order[0])
    head_node.left = build_tree_helper(pre_order, l1+1, l1+idx-l2, in_order, l2, idx-1)
    head_node.right = build_tree_helper(pre_order, l1+idx-l2+1, r1, in_order, idx+1, r2)
    return head_node

