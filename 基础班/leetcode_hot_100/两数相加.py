# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return []
        number_1 = self.get_number(l1)
        number_2 = self.get_number(l2)
        number = number_1 + number_2
        new_head = ListNode(0)
        result = new_head
        if number == 0:
            temp = ListNode(0)
            return temp
        while number > 0:
            temp = number % 10
            new_node = ListNode(temp)
            new_head.next = new_node
            new_head = new_node
            number = number // 10
        return result.next

    def get_number(self, L: Optional[ListNode]) -> int:
        number = 0
        temp = L
        k = 0
        while temp is not None:
            number += (temp.val) * (10 ** k)
            k += 1
            temp = temp.next
        return number







# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return None
        sum_1, sum_2 = 0, 0
        k1, k2 = 0, 0
        while l1:
            sum_1 += l1.val * (10 ** k1)
            l1 = l1.next
            k1 += 1
        while l2:
            sum_2 += l2.val * (10 ** k2)
            l2 = l2.next
            k2 += 1
        sum = sum_1 + sum_2
        if sum == 0:
            return ListNode(0)
        k = 1
        result_node = ListNode(0)
        temp_node = result_node
        while sum:
            temp = sum % 10
            new_node = ListNode(temp)
            temp_node.next = new_node
            temp_node = temp_node.next
            sum = sum // 10
        return result_node.next




















