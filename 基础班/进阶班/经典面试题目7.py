# LRU 内存替换算法
# put get 刷新时间操作  两个方法
# 双指针链表   时间复杂度是 o1
from tabnanny import check
import this


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 伪头、伪尾，避免边界判断
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)   # 访问过 → 移到头部
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self.add_to_head(new_node)
            self.size += 1
            if self.size > self.capacity:
                # 删除尾部节点
                removed = self.remove_tail()
                del self.cache[removed.key]
                self.size -= 1

    # 加到头部（最近使用）
    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # 移除节点
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 移到头部 = 先删再加
    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    # 删除尾部（最久未使用）
    def remove_tail(self):
        res = self.tail.prev
        self.remove_node(res)
        return res




# 双链表加 哈希表



#越靠近尾部 越是最新的  删除最不常用的节点

class ListNode:
    def __init__(self, key, value):
        self.key = None
        self.value = None
        self.next = None
        self.pre = None
class LRUCache:
    def __init__(self, key, ):
        self.head = ListNode()
        self.tail = ListNode()
        self.hash_map = {}
        self.capility
        self.size = 0
        self.head.pre = None
        self.head.next = self.tail
        self.tail.pre = self.head
        self.tail.next = None
    def get(self, key: int):
        if key not in self.hash_map:
            return 
        else:
            node = self.hash_map[key]
            self.move_node_to_tail(node)
        return 
    def set(self, key, value):
        if key in self.hash_map:
            self.hash_map[key].value = value
            return 
        else:
            new_node = ListNode(key=key, value=value)
            self.add(new_node)
            self.size += 1
            if self.size >= self.capility:
                self.remove_tail()
            return 

    def remove(self, node: ListNode):
        if not node:
            return 
        pre_node = node.pre
        next_node = node.next
        pre_node.next = next_node
        next_node.pre = pre_node
        return     
    def add(self, node: ListNode):
        if not node:
            return 
        #往尾部插入
        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node
        return 
    def move_node_to_tail(self, node: ListNode):
        if not node or node == self.tail or node == self.head:
            return
        self.remove(node)
        self.add(node)
        return 
    def remove_head(self):
        if self.head.next == self.tail:
            return 
        self.head.next = self.head.next.next
        self.head.next.next.pre = self.head
        return 
    def remove_tail(self):
        if self.head.next == self.tail:
            return 
        pre_node = self.tail.pre.pre
        pre_node.next = self.tail
        self.tail.pre = pre_node
        return 






# start 变成to  每次只能改变一个字符  list是中间路径列表
from typing import List
def zuiduanbianhuan(start: str, end: str, list: List[str]):
    if not start or list:
        return []
    def check_vaild(middle: str, list: List[str]):
        #返回在list列表当中  middle可以一步到达的选择
        result = []
        for i in range(len(list)):
            temp = list[i]
            count = 0
            for k in range(len(temp)):
                if temp[k] != middle[k]:
                    count += 1
            if count == 1:
                result.append(i)
        return result
    min_foot = float("inf")
    def process(zhongjian: str, list: List[str], temp_foot: int):
        if zhongjian == end:
            min_foot = min(min_foot, temp_foot)
        check_list = check_vaild(zhongjian, list)
        for i in range(len(check_list)):
            process(check_list[i], list, temp_foot + 1)
    process(start, list, 0)
    return min_foot


from typing import List
def zuiduanbianhuan(start: str, end: str, list: List[str]):
    if not start or list:
        return []
    #把list转成hash_set
    def change_hashj_set(list: List[str],):
        hash_map = {}
        for i in range(len(list)):
            hash_map[list[i]] == 1
        return hash_map
    hash_map = change_hashj_set(list)

    zimu_map = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z"
    ]
    def shengchenglinjubiao(list: List[str], hash_map: dict, zimu_map: dict):
        result = []
        for i in range(len(list)):
            temp = []
            #str的长度是j
            huanyuan = list[i]
            for j in range(len(list[0])):
                for houxuan in zimu_map:
                    if houxuan == list[i][j]:
                        continue
                    else:
                        list[i][j] = houxuan
                        if list[i] in hash_map:
                            temp.append(list[i])
                list[i] = huanyuan
            list[i] = huanyuan
            result.append(temp)
        return result
    linju = shengchenglinjubiao(list, hash_map, zimu_map,)
    #得到了邻居矩阵
    #使用宽度优先遍历  来找出
    def get_lingjumen(cankao: str, linju: List[List[str]]):
        zishenlinju = []
        for i in range(len(list)):
            if list[i] == cankao:
                return linju[i]
        
    def search(start: str, linju: List[List[str]], end: str):
        #参考宽度优先遍历
        from typing import Deque
        deque = Deque()
        deque.append([start, 0])
        temp_hash_map = {}
        temp_hash_map[start] = True
        while deque:
            deque_pop = deque.popleft()
            if deque_pop[0] == end:
                return deque_pop[1]
            distance = deque_pop[1]
            dangqianlingju = get_lingjumen(deque_pop[0], linju)
            for i in range(len(dangqianlingju)):
                if dangqianlingju[i] not in temp_hash_map:
                    dangqianlingju[i] = True
                    deque.append([dangqianlingju[i], distance+1])
