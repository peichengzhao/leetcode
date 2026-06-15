# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        if length == 0:
            return head
            
        k = k % length
        if k == 0:
            return head
        temp = length - k - 1
        cur = head
        while temp:
            cur = cur.next
            temp -= 1
        new_head = cur.next
        cur.next = None
        tail = new_head
        temp = k - 1
        while temp:
            tail = tail.next
            temp -= 1
        tail.next = head
        return new_head