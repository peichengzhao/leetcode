# 数组累加和问题



# uuid 原理上没有重复的id 大量使用


#  arr 数组 正数  sum
from typing import List

def get_max_length_1(arr: List[int], sum: int):
    pre_sum = [] * len(arr)
    sum = 0
    max_length = 0
    for i in range(len(arr)):
        sum += arr[i]
        pre_sum[i] = sum
    for k in range(len(pre_sum-1), 0, -1):
        for j in range(k-1, 0 ,-1):
            if pre_sum[k] - pre_sum[j] == sum:
                max_length = max(k - j + 1, max_length)
    return max_length

def get_max_length(arr: List[int], sum: int):
    window_sum = 0 
    # 仅仅限于正数可以
    # w < sum R ->
    # w > sum L -> 
    # w == sum 更新  R->
    left, right = 0, 0
    max_length = 0
    temp_sum = arr[0]
    while left <= right and right < len(arr):
        if temp_sum < sum:
            right += 1
            if right < len(arr):
                break
            temp_sum += arr[right]
        elif temp_sum > sum:
            temp_sum -= arr[left]
            if left > right:
                break
            left += 1
        else:
            max_length = max(max_length, right-left+1)
            temp_sum -= arr[left]
            temp_sum += arr[right]
            left += 1
            right += 1
    return max_length






# arr 有正有负有0
from typing import List

def get_max_length(arr: List[int], target_sum: int) -> int:
    """
    优化版：哈希表记录前缀和首次出现的索引，O(n)时间复杂度
    """
    if not arr:
        return 0
    
    # key: 前缀和，value: 该前缀和首次出现的索引（保留首次出现，才能得到最长子数组）
    pre_sum_map = {0: -1}  # 关键：前缀和0出现在索引-1，处理从开头的子数组
    current_sum = 0
    max_length = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        # 核心逻辑：找current_sum - target_sum是否在哈希表中
        if (current_sum - target_sum) in pre_sum_map:
            # 子数组长度 = 当前索引i - 前缀和首次出现的索引
            current_length = i - pre_sum_map[current_sum - target_sum]
            max_length = max(max_length, current_length)
        
        # 仅记录前缀和首次出现的索引（后续出现同一前缀和，不更新，保证子数组最长）
        if current_sum not in pre_sum_map:
            pre_sum_map[current_sum] = i
    
    return max_length



#
def get_k_length(arr: List[int], K: int):
    if not arr:
        return -1
    # 利用两个数组 搭配使用
    min_sum = [0] * len(arr)
    min_sum_end = [0] * len(arr)
    min_sum[len(arr)-1] = arr[len(arr) - 1]
    min_sum_end[len(arr) - 1] = len(arr) - 1
    for i in range(len(arr) - 2, -1, -1):
        if min_sum[i+1] <= 0:
            min_sum[i] = min_sum[i+1] + arr[i]
            min_sum_end[i] = min_sum_end[i+1]
        else:
            min_sum[i] = arr[i]
            min_sum_end[i] = i
    max_length = 0
    current_sum = 0
    begin = 0
    end = 0
    while begin < len(arr) and end < len(arr) and begin <= end:
        if min_sum[end] > K:
            end += 1
            begin = end
            current_sum = 0
            continue
        temp_sum = current_sum + min_sum[end]
        if temp_sum <=K:
            current_sum = temp_sum
            current_end = min_sum_end[end]
            max_length = max(max_length, current_end,- begin + 1)
            end = current_end + 1
        else:
            current_sum -= arr[begin]
            begin += 1
    return max_length


















