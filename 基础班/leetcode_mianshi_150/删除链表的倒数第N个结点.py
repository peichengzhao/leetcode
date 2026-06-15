# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        pre = ListNode(0)
        pre.next= head
        slow = fast = pre
        n = n+1
        while n and fast:
            fast = fast.next
            n -= 1
        if n>0 and not fast:
            return slow
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return pre.next