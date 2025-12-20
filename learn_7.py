

# leetcode 23 合并K个升序链表

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        import heapq
        min_heap = []
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, idx, node))
        result_head = ListNode(0)
        temp = result_head
        while min_heap:
            val, number, node = heapq.heappop(min_heap)
            temp.next = node
            temp = temp.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, number, node.next))
        return result_head.next