# 前缀树


class InfroNode:
    def __init__(self):
        self.pass_num = 0
        self.end_num = 0
        self.nexts = []




class Tree:
    def __init__(self):
        self.root = InfroNode()
    
    def insert(self, word: str):
        if word is None:
            return
        foot = self.root # 引用位置
        foot.pass_num += 1
        for i in range(len(word)):
            index = word[i] - 'a'
            if foot.nexts[index] == None:
                new = InfroNode()
                new.pass_num += 1
                foot = foot.nexts[index]
                foot.pass_num += 1
            else:
                foot = foot.nexts[index]
                foot.pass_num += 1
        foot.end_num += 1
    def search(self, word: str):
        if word is None:
            return 0
        foot = self.root
        for i in range(len(word)):
            index = word[i] - 'a'
            if foot.nexts[index] == None:
                return 0
            foot = foot.nexts[index]
        return foot.end_num
    
    def delete(self, word: str):
        if word is None:
            return 
        if self.search(word) == 0:
            return 
        foot = self.root
        for i in range(len(word)):
            index = word[i] - 'a'
            if foot.nexts[index].pass_num == 1:
                foot.nexts[index] = None
                return
            foot = foot.nexts[index]
            foot.pass_num -= 1
        foot.end_num -= 1