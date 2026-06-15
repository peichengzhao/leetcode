#一个数组  有多少个域

from typing import List

# 并查集
class UnionFind:
    # 初始化：n个元素，每个元素自己是父节点，秩（树高）为1
    def __init__(self, size):
        self.parent = list(range(size))  # 父节点数组
        self.rank = [1] * size           # 秩：记录树的高度/大小

    # 查找根节点 + 路径压缩
    def find(self, x):
        if self.parent[x] != x: # if self.parent[x] == x 说明x 是
            # 路径压缩：直接指向根节点
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 合并两个集合 + 按秩合并
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        #  already in the same set
        if root_x == root_y:
            return False
        
        # 按秩合并：小树挂到大树下
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            # 如果树高相同，合并后树高+1
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
        return True

    # 判断两个元素是否连通
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)





































