# bfprt算法
from typing import List
# 思路参考快速排序?

import random

def bfprt(list: List[int], k: int):
    if not list or k < 1 or k > len(list):
        return None
    return process2(list, 0, len(list)-1, k-1)



def process2(arr: list[int], l: int, r: int, index: int):
    if l ==r: # l == r == index
        return arr[l]
    pivot = arr[l + random.randint(0, r - l)]
    p_range = partition(arr, l, r, pivot)
    if index < p_range[0]:
        return process2(arr, l, p_range[0] - 1, index)
    elif index > p_range[1]:
        return process2(arr, p_range[1] + 1, r, index)
    else:
        return arr[range[0]]


def partition(arr: list[int], l: int, r: int, pivot: int):
    less = l - 1
    more = r + 1
    index = l
    while index < more:
        if arr[index] < pivot:
            less += 1
            change(arr, index, less)
            index += 1
        elif arr[index] > pivot:
            more -= 1
            change(arr, index, more)
            index += 1
        else:
            index += 1
    return less + 1, more - 1


def change(arr: list[int], i: int, j: int):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
        
def main(arr: list[int], k: int):
    if not arr or k < 1 or k > len(arr):
        return None
    return bfprt2(arr, 0, len(arr)-1, k-1)

def bfprt2(arr: list[int],l: int, r: int,  k: int):
    if not arr or k < 1 or k > len(arr):
        return None
    if l ==r :
        return arr[l]
    pivot = medianofmedians(arr, l, r)
    p_range = partition(arr, l, r, pivot)
    if k < p_range[0]:
        return bfprt2(arr, l, p_range[0] - 1, k)
    elif k > p_range[1]:
        return bfprt2(arr, p_range[1] + 1, r, k)
    else:
        return arr[p_range[0]]

def medianofmedians(arr: list[int], l: int, r: int):
    size = r - l + 1
    offset = 0 if size % 5 == 0 else 1
    medians = [0] * (size // 5 + offset)
    for i in range(len(medians)):
        start_i = l + i * 5
        end_i = min(start_i + 5, r + 1)
        medians[i] = bfprt2(arr, start_i, end_i - 1, start_i + (end_i - start_i) // 2)
    return bfprt2(medians, 0, len(medians) - 1, len(medians) // 2)





def find_xuanzhuan(str_1: str, str_2:str):
    if not str_1 or not str_2:
        return False
         
# bfprt算法

# arr 无序    找到第K小  O（n）拿下
# 可以参考排序玩

def bfprt(arr: List, k: int):
    if not arr or k < len(arr):
        return None
    


def process(arr: List, left: int, right: int, index: int):
    if left == right:
        return arr[left]
    pivot = arr[left + random.randint(right-left+1)]
    range_list = partition(arr, left, right, pivot)
    if index >= range_list[0] and index <= range_list[1]:
        return arr[index]
    elif index < range_list[0]:
        return process(arr, left, range_list[0] - 1, index)
    else:
        return process(arr, left, range_list[1] + 1, index)





def quan_pailie(arr: List[int]):
    if not arr:
        return None
    results = []
    arr = arr.sort()
    used = [False] * len(arr)

    def process(path: List[int]):
        if len(path) == len(arr):
            results.append(path.copy())
            return 
        for i in range(len(arr)):
            if used[i] == True:
                continue
            if i > 0 and arr[i] == arr[i-1] and not used[i-1]: #避免重复数字  
                continue
            used[i] = True
            path.append(used[i])
            process(path)
            path.pop()
            used[i] = False
    process([])
    return results
    


def zuichanghuiwenzichuan(str:)




















