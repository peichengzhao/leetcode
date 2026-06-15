# 链表     首先注重时间复杂度  尽量估计空间复杂度
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def return_middle_node(head: Node):
    if head == None or head.next == None or head.next.next == None:
        return head
    slow = head.next
    fast = head.next 
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverse_list(head: Node):
    if head == None or head.next == None:
        return head
    pre = None
    cur = head.next
    while cur != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    head = pre
    return head

def is_reversse_list(head: Node):
    if head == None or head.next == None:
        return True
    middle_node = return_middle_node(head)
    reverse_head = reverse_list(middle_node.next)
    while reverse_head != None:
        if reverse_head.value != head.value:
            moddle = reverse_list(reverse_head)
            middle_node.next = moddle
            return False
        reverse_head = reverse_head.next
        head = head.next
    reverse_list(reverse_head)
    middle_node.next = moddle
    return True

def change_list(head: Node, value: int):
    if head == None:
        return head
    small_head, small_tail, equal_head, equal_tail, big_head, big_tail = None, None, None, None, None, None
    while head != None:
        if head.value < value:
            if small_head == None:
                small_head = head
                small_tail = head
            else: 
                small_tail.next = head
                small_tail = head
        elif head.value == value:
            if equal_head == None:
                equal_head = head
                equal_tail = head
            else:
                equal_tail.next = head
                equal_tail = head
        else:
            if big_head == None:
                big_head = head
                big_tail = head
            else:
                big_tail.next = head
                big_tail = head
        head = head.next
    if small_tail != None:
        if equal_head != None:
            small_tail.next = equal_head
        else:
            small_tail.next = big_head
    if equal_tail != None:
        equal_tail.next = big_head
    if big_tail != None:
        big_tail.next = None
    if small_head == None:
        return small_head
    if equal_head == None:
        return equal_head
    return big_head


class Node_new: 
    def __init__(self, value):
        self.value = value
        self.next = None
        self.random = None

def clone_list(head: Node_new):
    if head == None:
        return head
    hash_map = {}
    cur = head
    while cur != None:
        new_node = Node_new(cur.value)
        map.add(cur, new_node)
        cur = cur.next
    cur = head
    while cur != None:
        temp = hash_map.get(cur)
        temp.next = hash_map.get(cur.next)
        temp.random = hash_map.get(cur.random)
        cur = cur.next
    return hash_map.get(head)


def clone_list_2(head: Node_new):
    if head == None:
        return head
    cur = head
    while cur != None:
        temp = Node_new(cur.value)
        next = cur.next
        cur.next = temp
        temp.next = next
        cur = next
    cur = head
    new_cur = head.next
    while cur != None:
        new_cur.random = cur.random.next
        cur = cur.next.next
        if cur != None:
            new_cur = cur.next
    cur = head
    new_cur = cur.next
    while cur != None:
        cur.next = new_cur.next
        new_cur.next = cur.next.next
        cur = cur.next
        if cur != None:
            new_cur = cur.next
    return new_cur



def cross_list(head1: Node, head2: Node):
    if head1 == None or head2 == None:
        return None
    loop1 = return_loop_node(head1)
    loop2 = return_loop_node_2(head2)
    if loop1 == None and loop2 == None: #双方都没有环

        #如果相交 最后必须是公共部分
        cur1 = head1
        cur2 = head2
        while cur1 != None and cur2 != None and cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        if cur1 == cur2:
            return cur1
        count = 0
        long = None
        short = None
        while cur1 != None:
            long = head1
            short = head2
            count += 1
            cur1 = cur1.next
        while cur2 != None:
            long = head2
            short = head1
            count += 1
            cur2 = cur2.next
        if cur1 != cur2:
            return None
        while count > 0:
            long = long.next
            count -= 1
        while long != short:
            long = long.next
            short = short.next
        return long
    if (loop1 == None and loop2 != None) or (loop1 != None and loop2 == None):
        return None
    if loop1 != None and loop2 != None: # 双方都有环
        if loop1 == loop2:
            # 通过长度来求出第一个公共节点
            
def return_loop_node(head: Node):
    if head == None or head.next == None:
        return None
    hash_map = {}
    cur = head
    while cur != None:
        hash_map.add(cur)
        cur = cur.next
        if cur in hash_map:
            return cur
    return None
def return_loop_node_2(head: Node):
    if head == None or head.next == None:
        return None
    slow = head.next 
    fast = head.next.next
    while fast != None and fast.next != None:
        if slow == fast:
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        slow = slow.next
        fast = fast.next.next
    return None



