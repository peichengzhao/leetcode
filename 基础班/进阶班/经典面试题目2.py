from curses import noecho
from tkinter import NO
from typing import List

from 进阶班.经典面试题目1 import max_length



def build_list(N: int):
    if N <= 2:
        return []
    halfsize = N // 2
    results = []
    for i in range(halfsize):
        results.append(i * 2)
    for j in range(halfsize):
        results.append(i * 2 + 1)
    results = results[:N - 1]
    return results



class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


def search_tree(node: Node):
    if not node:
        return 0
    max_sum = [float('-inf')]
    def process(node: Node, temp_sum: int):
        if node == None:
            return
        max_sum = max(max_sum[0], temp_sum)
        if temp_sum < 0:
            temp_sum = node.value
        else:
            temp_sum += node.value
        process(node.left, temp_sum)
        process(node.right, temp_sum)
    max_sum = float('-inf')
    max_sum = process(node, 0)
    return max_sum[0]


#打包机器人
import math

def robot_bag(arr: List[int]):
    if not arr:
        return -1
    sum = 0 
    for i in range(len(arr)):
        sum += arr[i]
    if sum % len(arr) != 0:
        return -1
    step = 0
    high_list = []
    for i in range(len(arr)):
        if arr[i] > sum // len(arr):
            high_list.append([i, arr[i]])
    def find_near(arr: List[int], i, high_list):
        min_dist = float('inf')
        pos = -1
        for j in range(len(high_list)):
            if high_list[j][1] - sum // len(arr) > 0:
                dist = abs(i - high_list[j][0])
                if dist < min_dist:
                    min_dist = dist
                    best_pos = j
        if best_pos == -1:
            return 0
        high_list[best_pos][1] -= 1
        return min_dist
    for i in range(len(arr)):
        if arr[i] >= sum // len(arr):
            continue
        chazhi = sum // len(arr) - arr[i]
        while chazhi > 0:
            step += find_near(arr, i, high_list)
            chazhi -= 1
    return step




def robot_bag(arr: List[int]):
    if not arr:
        return -1
    sum = 0 





# 找到max_value 和最左边最右边比较
def find_max_value(arr: List[int]):
    if len(arr) <= 1:
        return -1
    max_value = arr[0]
    for i in range(len(arr)):
        max_value = max(max_value, arr[i])
    return max_value - arr[0] if arr[0] <= arr[len(arr) - 1] else max_value - arr[len(arr) - 1]
















