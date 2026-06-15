from re import search
from typing import List, Optional



class Node:
    def __init__(self, value):
        self.val = value
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.begin = Node(None)

    def addWord(self, word: str) -> None:
        temp = self.begin
        for c in word:
            if c not in temp.children:
                temp.children[c] = Node(c)
            temp = temp.children[c]
        temp.is_end = True

    def search(self, word: str) -> bool:
        temp = self.begin
        for i in range(len(word)):
            if word[i] not in temp.children and word[i] != ".":
                return False
            elif word[i] in temp.children:
                temp = temp.children[word[i]]
            else: # c == "."
                if len(temp.children) == 0:
                    return False
                candidate = temp.children
                result = False
                for can in candidate:
                    result = self.search(word=word[:i] + can + word[i+1:]) or result
                return result
        return True if temp.is_end else False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)