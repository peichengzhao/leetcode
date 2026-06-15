from hmac import new
from math import e
from tkinter import NO

from pydantic import NonPositiveFloat


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# 单链表和双链表的反转

def reverse_single_list(head: Node):
    if head is None:
        return None
    pre = None
    cur = head
    next = head.next
    while next is not None:
        cur.next = pre
        pre = cur
        cur = next
        next = cur.next
    return cur




def delete_node(head: Node, value: int):
    if head is None:
        return head
    if head.value == value:
        while(head is not None and head.value == value):
            head = head.next
        return head
    cur = head
    while cur.next is not None and cur.next.value != value:
        cur = cur.next
    if cur.next is not None:
        temp = cur.next
        while temp is not None and temp.value == value:
            temp = temp.next
        cur.next = temp
    return head


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.last = None



class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_head(self, value: int):
        new_node = DoubleNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.last = new_node
            self.head = new_node
    def add_tail(self, value:int):
        new_node = DoubleNode(value)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.last = self.tail
            self.tail.next = new_node
            self.tail = new_node
    def delete_head(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            return temp
        else:
            temp = self.head
            self.head.next.last = None
            self.head = self.head.next
            temp.next = None
        return temp
    def delete_tail(self):
        if self.tail is None:
            return None
        if self.head == self.tail:
            temp = self.tail
            self.tail = None
            self.head = None
            return temp
        else:
            temp = self.tail
            self.tail.last.next = None
            self.tail = self.tail.last
            temp.last = None
            return temp 
