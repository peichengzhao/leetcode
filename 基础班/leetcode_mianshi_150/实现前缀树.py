
class Node:
    def __init__(self, value) -> None:
        self.children = {}
        self.is_node = False

class Trie:
    def __init__(self):
        self.begin_node = Node()

    def insert(self, word: str) -> None:
        temp = self.begin_node
        for c in word:
            if c in temp.children:
                temp = temp.children[c]
            else:
                temp.children[c] = Node()
                temp = temp.children[c]
        temp.is_node = True
    def search(self, word: str) -> bool:
        temp = self.begin_node
        for c in word:
            if c in temp.children:
                temp = temp.children[c]
                continue
            else:
                return False
        return True if temp.is_node else False

    def startsWith(self, prefix: str) -> bool:
        temp = self.begin_node
        for c in prefix:
            if c in temp.children:
                temp = temp.children[c]
                continue
            else:
                return False
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)