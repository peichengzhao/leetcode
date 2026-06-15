# morris代码



class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def morris(head: Node):
    if head is None:
        return None
    cur = head
    most_right = None
    while cur:
        if not cur.left:
            print(cur.val)
            cur = cur.right
        else:
            most_right = cur.left
            while most_right.right and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                most_right.right = cur
                cur = cur.left
            else:
                most_right.right = None
                print(cur.val)
                cur = cur.right
    return 
