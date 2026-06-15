# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: ListNode):
        if head is None or head.next is None:
            return head
        cur_node = head
        next_node = cur_node.next
        pre_node = None
        while next_node is not None:
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
            next_node = next_node.next
        cur_node.next = pre_node
        return cur_node







# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        pre, cur, next = None, head, head.next
        while next:
            cur.next = pre
            pre = cur
            cur = next
            next = next.next
        cur.next = pre
        return cur

        




















