# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        help_list = []
        temp = head
        while temp:
            help_list.append(temp.val)
            temp = temp.next
        help_list = sorted(help_list)
        result = ListNode(help_list[0])
        temp = result
        for i in range(1, len(help_list)):
            temp.next = ListNode(help_list[i])
            temp = temp.next
        return result


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # 利用合并两个有序链表实现
    def merge(self, head1: Optional[ListNode], head2: Optional[ListNode]):
        while head1 and head2:
            result = ListNode(0)
            temp = result
            if head1.val <= head2:
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next
        temp.next = head1 if head1 else head2
        return result.next
    def find_middle(self, node: Optional[ListNode]):
        slow = fast = node
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return slow
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head2 = self.find_middle(head)
        head = self.sortList(head)
        head2 = self.sortList(head2)
        return self.merge(head, head2)

