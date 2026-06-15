# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        head1, head2 = list1, list2
        result_node = ListNode()
        temp = result_node
        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next
        if head1 is not None:
            temp.next = head1
        else:
            temp.next = head2
        return result_node.next