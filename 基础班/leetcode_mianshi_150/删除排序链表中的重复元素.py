# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left = right = head
        while right:
            while right.val == left.val:
                right = right.next
                if right == None:
                    break
            left.next = right
            left = right 
        return head




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = ListNode(0)
        new_head.next = head
        left, right = head, head.next
        pre = new_head
        while right:
            if left.val == right.val:
                while right.val == left.val:
                    right = right.next
                    if right == None:
                        break
                pre.next = right
                left = right
                if right:
                    right = right.next
            else:
                pre.next = left
                pre = pre.next
                left = right
                right = right.next
        return new_head.next
