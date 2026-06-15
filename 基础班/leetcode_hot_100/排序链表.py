# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        help_list = []
        temp = head
        while temp:
            help_list.append(temp.val)
            temp = temp.next
        temp = head
        help_list = sorted(help_list)
        for i in range(len(help_list)):
            temp.val = help_list[i]
            temp = temp.next
        return head


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        temp_length = 1
        res = ListNode(0)
        middle_node = self.find_middle(head)
        self.process(head, middle_node)

    
    def find_middle(self, head: ListNode):
        if not head.next:
            return head
        slow, fast = head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return slow 
    def merge(self, head_1: ListNode, head_2: ListNode):
        if not head_1 and head_2:
            return 
        if not head_1:
            return head_2
        if not head_2:
            return head_1
        res = ListNode(0)
        temp = res
        while head_1 and head_2:
            if head_1.val < head_2.val:
                temp.next = head_1
                head_1 = head_1.next
            else:
                temp.next = head_2
                head_2 = head_2.next
            temp = temp.next
        if head_1:
            temp.next = head_1
        if head_2:
            temp.next = head_2
        return res.next
    def process(self, head: ListNode):
        if not head or not head.next:
            return head
        head_2 = self.find_middle(head)
        head = self.process(head)
        head_2 = self.process(head_2)
        return self.merge(head, head_2)