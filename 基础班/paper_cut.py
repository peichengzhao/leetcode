# def paper_cut(N: int):
#     print_process(1, N, True)
#     return 

# def print_process(i: int, N: int, cut: bool):
#     if i > N:
#         return
#     print_process(i+1, N, True)
#     print(cut)
#     print_process(i+1, N, False)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.left = None


def process(head: Node):
    if head == None:
        return true, 0
    left_ping, left_height = process(head.left)
    right_ping, right_height = process(head.right)
    is_ping = left_ping and right_ping and abs(left_height - right_height) <= 1
    height = max(left_height, right_height) + 1
    return is_ping, height

def is_ping_tree(head: Node):
    is_ping, height = process(head)
    return is_ping


class Employee:
    def __init__(self, happy: int, subordinates: list):
        self.happy = happy
        self.subordinates = subordinates


