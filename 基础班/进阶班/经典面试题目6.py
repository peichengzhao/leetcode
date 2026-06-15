# arr 返回最大累加和

from multiprocessing import Value
from typing import List

from 进阶班.经典面试题目2 import Node
def get_pre_arr(arr: List[int]):
    if not arr:
        return None
    pre_arr = [0]
    temp = 0
    for i in range(len(arr)):
        temp += arr[i]
        pre_arr.append(temp)
    return pre_arr

def fanhuizuida(arr: List[int]):
    if not arr:
        return -1
    # 得到前缀数组和
    pre_arr = get_pre_arr(arr)
    # max_value = pre_arr[-1]
    min_value = pre_arr[0]
    max_value = float('-inf')
    for i in range(1, len(pre_arr)):
        max_value = max(max_value, pre_arr[i] - min_value)
        min_value = min(min_value, pre_arr[i])
    return max_value

def fanhuizuidazhi(arr: List[int]):
    if not arr:
        return None
    cur = 0
    max_value = float('-inf')
    for i in range(len(arr)):
        cur = cur + arr[i] if cur + arr[i] >=0 else 0
        max_value = max(cur, max_value)
    return max_value



#对于矩阵的 最大子矩阵求解
def fanhuizuidazhijuzhen(arr: List[List[int]]):
    if not arr:
        return None
    row, col = len(arr), len(arr[0])
    for i in range(row):
        for j in range(i, row):
            help_list = arr[i]
            temp = j 
            while temp > i:
                for k in range()






# 双向链表节点和二叉树节点的结构是很相似的

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Node:
    def __init__(self, value):
        self.value = value
        self.last = None
        self.next = None
 
def middle_process(head: Node):
    if head == None:
        return None, None
    left_head, left_tail = middle_process(head.left)
    right_head, right_tail = middle_process(head.right)
    head.next = right_head
    head.last = left_tail
    if left_tail:
        left_tail.next = head
    if right_head:
        right_head.last = head
    new_head = left_head if left_head else head
    new_tail = right_tail if right_tail else head
    return new_head, new_tail



# 给 str_1 str_2 三个操作 ic dc rc 插入 删除和替换  返回 str_1 -> str_2 的最小代价

def min_daijia(str_1: str, str_2: str, ic: int, dc: int, rc: int):
    #编辑距离问题
    #动态规划问题
    dp = [[0] * (len(str_2)+1) for _ in range(len(str_1)+1)]
    for j in range(len(str_2)+1):
        dp[0][j] = j * ic
    for i in range(len(str_1)+1):
        dp[i][0] = i * dc    
    #分情况
    # 1 i-1 j-1
    for i in range(1, len(str_1)):
        for j in range(1, len(str_2)):
            if str_1[i-1] == str_2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + rc # 替换
            dp[i][j] = min(dp[i][j], dp[i][j-1] + ic) #增加
            dp[i][j] = min(dp[i][j], dp[i-1][j] + dc) # 删除

    return dp[len(str_1)][len(str_2)]