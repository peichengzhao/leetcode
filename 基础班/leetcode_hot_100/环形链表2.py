# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 相遇则说明有环，跳出循环处理入口
            if slow == fast:
                break
        # 3. 无环的情况：fast走到末尾，直接返回None
        if not fast or not fast.next:
            return None
        
        # 4. 找环的入口：重置一个指针到head，双指针同速(都走1步)前进
        fast = head
        while fast != slow:
            fast = fast.next  # 修正：快指针改为走1步
            slow = slow.next  # 慢指针保持走1步
        
        # 相遇点就是环的入口
        return fast













class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False 
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False

class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast


