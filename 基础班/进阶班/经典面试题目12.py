# 返回可整合数组的最大长度
from typing import List



def kezhenghe(arr: List[int]) -> int:
    if not arr:
        return 0
    max_len = 1
    n = len(arr)
    for i in range(n):
        s = set()
        cur_min = cur_max = arr[i]
        s.add(arr[i])
        for j in range(i+1, n):
            if arr[j] in s:
                break
            s.add(arr[j])
            cur_min = min(cur_min, arr[j])
            cur_max = max(cur_max, arr[j])
            if cur_max - cur_min == j - i:
                max_len = max(max_len, j-i+1)
    return max_len
#卡特兰数
# 联想 二叉树
# N个0 N个1  自由组合 2N个数  任何前缀0必须不要比1少
# 集合论的思想
#股票交易

def gupiao(arr: List[int]):
    if not arr:
        return 0
    result = 0
    min_value = arr[0]
    for i in range(1, len(arr)):
        result = max(result, arr[i] - min_value)
        min_value = min(arr[i], min_value)
    return result



def gupiao2(arr: List[int]):
    if not arr:
        return 0
    result = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            result += arr[i] - arr[i-1]
    return result
