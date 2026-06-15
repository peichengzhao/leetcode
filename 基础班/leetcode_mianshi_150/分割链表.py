# Definition for singly-linked list.
from cgitb import small
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        samll = ListNode(0)
        small_node = small
        big = ListNode(0)
        big_node = big
        temp = head
        while temp:
            if temp.val < x:
                small_node.next = temp
                small_node = temp
            else:
                big_node.next = temp
                big_node = temp
            temp = temp.next
        small_node.next = big.next
        return small.next