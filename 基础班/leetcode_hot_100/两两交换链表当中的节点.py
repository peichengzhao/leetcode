# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        pre = None
        res = head.next
        cur_1, cur_2 = head, head.next
        foot = cur_2.next
        while cur_1 and cur_2:
            cur_1.next = foot
            cur_2.next = cur_1
            if pre:
                pre.next = cur_2
            cur_1 = foot.next
            pre = foot
            if cur_1:
                cur_2 = cur_1.next
            if cur_2:
                foot = cur_2.next
        return res




# 利用stack



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
	def swapPairs(self, head):
		if not (head and head.next):
			return head
		p = ListNode(-1)
		# 用stack保存每次迭代的两个节点
		# head指向新的p节点，函数结束时返回head.next即可
		cur,head,stack = head,p,[]
		while cur and cur.next:
			# 将两个节点放入stack中
			stack.append(cur),stack.append(cur.next)
			# 当前节点往前走两步
			cur = cur.next.next
			# 从stack中弹出两个节点，然后用p节点指向新弹出的两个节点
			p.next = stack.pop()
			p.next.next = stack.pop()
			p = p.next.next
		# 注意边界条件，当链表长度是奇数时，cur就不为空	
		if cur:
			p.next = cur
		else:
			p.next = None
		return head.next


