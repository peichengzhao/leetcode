class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None



def find_next_node(node: Node):
    if node == None:
        return None
    if node.right != None:
        temp = node.right
        while temp.left != None:
            temp = temp.left
        return temp
    else:
        parent = node.parent
        child = node
        while parent != None and parent.left != child:
            child = parent
            parent = parent.parent
        return parent

        
            