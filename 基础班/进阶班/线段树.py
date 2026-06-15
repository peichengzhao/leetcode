# 线段树

from typing import List
class xianduanshu:
    def __init__(self) -> None:
        return None

    def add(L ,R, arr, V):
        return 

    def update(L, R, arr, V):
        return 
    def get_sum(L, R, arr):
        return 
    def segment_tee(origin: List[int]):
        length = len(origin) + 1
        arr = [] * length
        for i in range(1, length):
            arr[i] = origin[i-1]
        sum = [] *(length << 2)
    
    def build(self, l ,r, rt, sum, arr):
        if l == r:
            sum[rt] = arr[l]
            return 
        mid = (l + r) >> 1
        self.build(l, mid, rt << 1)
        self.build(mid+1, r, rt << 1 | 1)
        sum[rt] = arr[rt << 1] + arr[rt << 1 | 1]
        return 
    