# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        temp1_node = headA
        temp2_node = headB
        length1 = 1
        length2 = 1
        while temp1_node.next is not None:
            length1 += 1
            temp1_node = temp1_node.next
        while temp2_node.next is not None:
            length2 += 1
            temp2_node = temp2_node.next
        if temp1_node != temp2_node:
            return None
        else:
            temp1_node = headA
            temp2_node = headB
            if length1 >= length2:
                temp = length1 - length2
                while temp > 0:
                    temp1_node = temp1_node.next
                    temp -= 1
                while temp1_node != temp2_node:
                    temp1_node = temp1_node.next
                    temp2_node = temp2_node.next
            else:
                temp = length2 - length1
                while temp > 0:
                    temp2_node = temp2_node.next
                    temp -= 1
                while temp1_node != temp2_node:
                    temp1_node = temp1_node.next
                    temp2_node = temp2_node.next
            return temp1_node








# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB :
            return None
        length_a, length_b = 1, 1
        node_a ,node_b = headA, headB
        while node_a.next:
            length_a += 1
            node_a = node_a.next
        while node_b.next:
            length_b += 1
            node_b = node_b.next
        if node_a != node_b:
            return None
        else:
            temp_b = headB
            temp_a = headA
            if length_a >= length_b:
                foot = length_a - length_b
                while (foot > 0):
                    temp_a = temp_a.next
                    foot -= 1
            else:
                foot = length_b - length_a
                while (foot > 0):
                    temp_b = temp_b.next
                    foot -= 1
            while temp_a != temp_b:
                temp_a = temp_a.next
                temp_b = temp_b.next
            return temp_a