
# 递归写法
from numpy import swapaxes
def merge_sort(list: list):
    if list == None or len(list) < 2:
        return list
    process(list, 0, len(list) - 1)
    return list
def process(list: list, left: int, right: int):
    if left == right :
        return 
    mid = left + ((right - left) >> 1)
    process(list, left, mid)
    process(list, mid+1, right)
    merge(list, left, mid, right)

def merge(list, left, mid, right):
    help = []
    p1 = left
    p2 = mid + 1
    while p1 <= mid and p2 <= right:
        if list[p1] <= list[p2]:
            help.append(list[p1])
            p1 += 1
        else:
            help.append(list[p2])
            p2 +=1
    while p1 <= mid:
        help.append(list[p1])
        p1 += 1
    while p2 <= right:
        help.append(list[p2])
        p2 += 1
    for i in range(len(help)):
        list[left + 1] = help[i]
# 非递归写法

import numpy as np
#快速排序
def quick_sort(list: list):
    lessequal = -1
    index = 0
    mostR = len(list) -1
    while index <= mostR:
        if list[index] <= list[mostR]:
            lessequal += 1
            change(list, lessequal, index)
        index += 1
    



def change(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    return  


test = [7, 1, 3, 5, 6, 7,3, 2, 4,6 ,3, 1, 5]

quick_sort(test)
print(test)

def partition(list, left, right):
    less = left - 1
    more = right + 1
    index = left
    temp = list[right]
    while index < more:
        if list[index] < list[temp]:
            less += 1
            change(list, less, index)
            index += 1
        if list[index] == list[temp]:
            index += 1
        if list[index] > list[temp]:
            more -= 1
            change(list, more, index)
    return less ,more

def quick_sort(list: list):
    if list == None or len(list) < 2:
        return
    process(list, 0, len(list) - 1)
    return list

def process(list: list, left: int, right: int):
    if left >= right:
        return
    less, more = partition(list, left, right)
    process(list, left, less)
    process(list, more, right)
    return 








