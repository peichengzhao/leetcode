#装 水问题
from typing import List
def max_water(arr: List[int]):
    if not arr: 
        return 0
    #利用辅助空间
    sum = 0
    left_max_list = [arr[0]]
    left_max = arr[0]
    right_max_list = [0] * len(arr)
    right_max_list[len(arr) - 1] = arr[len(arr) - 1]
    right_max = arr[len(arr) - 1]
    for i in range(1, len(arr)):
        if arr[i] > left_max:
            left_max = arr[i]
        left_max_list.append(left_max)
    for j in range(len(arr)-2, -1):
        if arr[j] > right_max:
            right_max = arr[j]
        right_max_list[j] = right_max
    for index in range(1, len(arr)-1):
        if arr[index] >= left_max_list[index-1] or arr[index] >= right_max_list[index+1]:
            continue
        sum += min(left_max_list[index-1], right_max_list[index+1]) - arr[index]
    return sum

def max_water(arr: List[int]):
    if not arr: 
        return 0
    #利用两个指针 分情况讨论
    sum = 0
    left_max, right_max = arr[0], arr[len(arr) - 1]
    left, right = 1 ,len(arr) - 2
    while left <= right:
        if left_max <= right_max and arr[left] < left_max:
            sum += left_max -  arr[left]
            left += 1
        elif left_max > right_max and arr[right] < right_max:
            sum += right_max - arr[right]
            right -= 1
        elif left_max <= right_max and arr[left] >= left_max:
            left_max = arr[left]
            left += 1
        elif left_max > right_max and arr[right] >= right_max:
            right_max = arr[right]
            right -= 1
    return sum

# 二维装水
import heapq

def get_2_water(arr: List[List[int]]):
    heap = [] 
    hash_map = {}
    hash_map[[0, 0]] = True
    hang_length = len(arr)
    lie_length = len(arr[0])
    for i in range(lie_length):
        high = arr[0][i]
        heapq.heappush(heap, (high, 0, i))
        hash_map[(0, i)] = True
    for j in range(1, hang_length):
        high = arr[j][lie_length-1]
        heapq.heappush(heap, (high, j, lie_length))
        hash_map[(j, lie_length)] = True
    for i in range(lie_length-2, -1, -1):
        high = arr[hang_length - 1][i]
        heapq.heappush(heap, (high, hang_length-1, i))
        hash_map[(j, lie_length)] = True
    for j in range(hang_length-2, 0, -1):
        high = arr[j][0]
        heapq.heappush(heap, (high, j, 0))
        hash_map[j][0] = True
    water = 0
    max_high = float('-inf')
    while heap:
        high, row, col = heapq.heappop(heap)
        max_high = max(high, max_high)
        if row > 0 and row < hang_length and (arr[row-1][col], row-1, col) not in hash_map:
            heapq.heappush(heap, (arr[row-1][col], row-1, col))
            hash_map[(row-1, col)] = True
        if col > 0 and (arr[row][col-1], row, col-1) not in hash_map:
            heapq.heappush(heap, (arr[row][col-1], row, col-1))
            hash_map[(row, col-1)] = True
        if row < hang_length-1 and (arr[row+1][col], row+1, col) not in hash_map:
            heapq.heappush(heap, (arr[row+1][col], row+1, col))
            hash_map[(row+1, col)] = True
        if col < lie_length and (arr[row][col+1], row, col+1) not in hash_map:
            heapq.heappush(heap, (arr[row][col+1], row, col+1))
            hash_map[(row, col+1)] = True
        if high < max_high:
            water += max_high - high
    return water


# 有序数组arr[] 返回和值为二元组
def get_two_sum(arr: List[int], target: int):
    left, right = 0, len(arr) - 1
    result = []
    while left < right:
        if arr[left] + arr[right] < target:
            left += 1
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            result.append([arr[left], arr[right]])
            while left + 1 < right and arr[left] == arr[left+1]:
                left += 1
            left += 1
            while left < right - 1  and arr[right] == arr[right - 1]:
                right -= 1
            right -= 1
    return result


# 有序数组arr[] 返回和值为三元组

def get__three_sum(arr: List[int], target: int):
    result = []

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        temp = target - arr[i]
        if temp >= 0:
            break
        get_two_sum(arr[i+1:len(arr)])
    return result





def min_dui(arr: List[int], k: int):
    sorted_arr = sorted(arr)
    result = []
    for i in range(len(sorted_arr)):
        for j in range(len(sorted_arr)):
            result.append([i, j])
            if len(result) == k:
                return result[-1]



def min_dui(arr: List[int], k: int):
    # 假设数组排过序了
    length = len(arr)
    number_1 = length // k #第几个数字是头
    number_2 = length % k
    help
    for i in range(len(arr)):
        











