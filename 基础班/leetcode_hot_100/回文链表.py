# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        middle_node = self.find_middle_node(head)
        reverse_head = self.reverse_list(middle_node.next)
        while reverse_head is not None:
            if reverse_head.val != head.val:
                return False
            reverse_head = reverse_head.next
            head = head.next
        return True

    def reverse_list(self, head: Optional[ListNode]):
        if head is None or head.next is None:
            return head
        pre = None
        cur = head
        next = head.next
        while next is not None:
            cur.next = pre
            pre = cur
            cur = next
            next = cur.next
        cur.next = pre
        return cur
    def find_middle_node(self, head: Optional[ListNode]):
        if head is None or head.next is None or head.next.next is None:
            return head
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow











# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        length = 1
        temp = head
        while temp:
            temp = temp.next
            length += 1
        if length % 2 == 1:
            return False
        foot = length / 2
        pre, cur, next = None, head, head.next
        while (foot - 1):
            cur.next = pre
            pre = cur
            cur = next
            next = next.next
        while cur and next:
            if cur.val != next.val:
                return False
        return True
        










