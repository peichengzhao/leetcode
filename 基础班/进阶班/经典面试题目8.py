# arr  返回所有的异数和 最大值
from tracemalloc import start
from typing import List



#生成异或和 按位异或 ^ 求最大子数组异或和
def max_sub_sum(arr: List[int]):
    if not arr:
        return -1
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
# 可以利用前缀 异或和
# n平方的时间复杂度
def return_yihuo(arr: List,):
    eor = [] * len(arr)
    eor[0] = arr[0]
    for i in range(len(arr)):
        eor[i] = eor[i-1] ^ arr[i]
    #得到了前缀异或和数组
    result = arr[0]
    for i in range(len(arr)):
        sum_temp = eor[i]
        for j in range(i-1, -1, -1):
            result = max(eor[i] ^ eor[j], result)
    return result
# 利用前缀树来解决

def return_yihuo(arr: List,):
    return 

class Trie:
    def __init__(self):
        self.children = {}  # 子节点：key=字符，value=子节点
        self.is_end = False # 标记：是否是一个完整单词的结尾

    # 插入单词
    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.is_end = True  # 单词结尾打标记

    # 查找完整单词
    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end # 必须走到结尾且标记为True

    # 查找是否有该前缀（最常用！）
    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
class Trie:
    # 节点类（写在内部，更整洁）
    class Node:
        def __init__(self):
            self.children = {}
            self.is_end = False

    # 初始化：自己创建根节点，不用全局变量！
    def __init__(self):
        self.root = self.Node()

    # 插入单词
    def insert(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = self.Node()
            node = node.children[c]
        node.is_end = True

    # 查找完整单词
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    # 查找前缀
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

