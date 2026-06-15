# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 0:
            return head
        slow, fast = head, head
        pre_tail = ListNode(0)
        first_time = True
        while fast:
            number = k
            while fast and number > 0:
                fast = fast.next
                number -= 1
            if not fast:
                pre_tail.next = slow 
                break
            new_head, new_tail = self.reverse(slow, k)
            if first_time:
                result = new_head
                first_time = False
            pre_tail.next = new_head
            pre_tail = new_tail
            slow = fast
        return result

    def reverse(self, head: Optional[ListNode], k: int):
        # 第一步：检查够不够k个，不够直接返回不翻转
        check = head
        for _ in range(k):
            if not check:
                return head, None  # 不够k个，不翻转
            check = check.next

        # 第二步：标准翻转k个节点
        pre = None
        cur = head
        for _ in range(k):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        # 翻转后：pre = 新头，head = 新尾
        return pre, head





class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 0:
            return head
        slow, fast = head, head
        pre_tail = ListNode(0)
        result = pre_tail
        while slow:
            for _ in range(k):
                if not fast:
                    pre_tail.next = slow
                    return result.next
                fast = fast.next
            new_head, new_tail = self.reverse(slow, k)
            pre_tail.next = new_head
            pre_tail = new_tail
            slow = fast
        
        return result.next 
            

    def reverse(self, head: Optional[ListNode], k: int):
        check = head
        for _ in range(k):
            if not check:
                return head, None
            check = check.next
        pre = None
        cur = head
        for _ in range(k):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre, head
