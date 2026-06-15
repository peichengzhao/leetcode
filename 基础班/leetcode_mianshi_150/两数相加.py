# Definition for singly-linked list.
from tkinter import NO
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        def deverse_node(node: Optional[ListNode]):
            if node == None:
                return None
            pre = None
            cur = node
            next = cur.next
            while cur:
                cur.next = pre
                pre = cur
                cur = next
                if next:
                    next = next.next
            return pre
        l1_node, l2_node = deverse_node(l1), deverse_node(l2)
        jinwei = False
        result_node = ListNode(0)
        temp_node = result_node
        while l1_node and l2_node:
            temp = l1_node.val + l2_node.val
            if jinwei == True:
                temp += 1
            if temp >= 10:
                jinwei = True
                temp = temp % 10
            else:
                jinwei = False
            temp_node.next = ListNode(temp)
            temp_node = temp_node.next
            l1_node = l1_node.next
            l2_node = l2_node.next
        while l1_node:
            temp = l1_node.val
            if jinwei:
                temp += 1
            if temp >= 10:
                jinwei = True
                temp = temp % 10
            else:
                jinwei = False
            temp_node.next = ListNode(temp)
            temp_node = temp_node.next
            l1_node = l1_node.next
        while l2_node:
            temp = l2_node.val
            if jinwei:
                temp += 1
            if temp >= 10:
                jinwei = True
                temp = temp % 10
            else:
                jinwei = False
            temp_node.next = ListNode(temp)
            temp_node = temp_node.next
            l2_node = l2_node.next
        if jinwei:
            temp_node.next = ListNode(1)
            temp_node = temp_node.next
        return deverse_node(result_node.next)





class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_value(node: Optional[ListNode]):
            res = 0
            count = 1
            while node:
                res += node.val * count
                count = count * 10
                node = node.next
            return res
        val1, val2 = get_value(l1), get_value(l2)
        result_val = val1 + val2
        if result_val == 0:
            return ListNode(0)
        pre = None
        result = ListNode(0)
        temp_node = result
        while result_val > 0:
            temp = result_val % 10
            result_val = result_val // 10
            new_node = ListNode(temp)
            temp_node.next = new_node
            temp_node = new_node
        return result.next

