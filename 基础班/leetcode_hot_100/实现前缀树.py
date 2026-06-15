from typing import List
import torch


class Trie:
    class Node:
        def __init__(self) -> None:
            self.chirdren = {}
            self.is_end = False
    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        if not word:
            return 
        node = self.root
        for c in word:
            if c not in node.chirdren:
                node.chirdren[c] = self.Node()
            node = node.chirdren[c]
        node.is_end = True
        return 

    def search(self, word: str) -> bool:
        if not word:
            return True
        node = self.root
        for c in word:
            if c not in node.chirdren:
                return False
            node = node.chirdren[c]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        node = self.root
        for c in prefix:
            if c not in node.chirdren:
                return False
            node = node.chirdren[c]
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)