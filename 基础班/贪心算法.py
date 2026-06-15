# 贪心算法
from tkinter import N


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class Info:
    def __init__(self, man, wanquan, height):
        self.man = man
        self.wanquan = wanquan
        self.height = height


def process(head: Node):
    if head == None:
        return Info(True, True, 0)
    left_info = process(head.left)
    right_info = process(head.right)
    height = max(left_info.height, right_info.height) + 1
    isfull = left_info.isfull and right_info.isfull and left_info.height == right_info.height
    isbalance = left_info.isbalance and right_info.isbalance and abs(left_info.height - right_info.height) <= 1
    return Info(isfull, isbalance, height)


def find_together_parent(head: Node, a: Node, b: Node, together_parent_head: N):
    if together_parent_head != None:
        return True, True
    if head == None:
        return False, False 
    if head == a:
        return True, False
    if head == b:
        return False, True
    left_have_a, left_have_b = find_together_parent(head.left, a, b, together_parent_head)
    right_have_a, right_have_b = find_together_parent(head.right, a, b, together_parent_head)
    have_a = left_have_a or right_have_a
    have_b = left_have_b or right_have_b
    if have_a and have_b:
        together_parent_head = head
    return have_a, have_b

def work(head: Node, a: Node, b: Node):
    if head == None:
        return None
    if head == a or head ==b:
        return head
    
    together_parent_head = None
    have_a, have_b = find_together_parent(head, a, b, together_parent_head)
    return together_parent_head

#贪心算法

