# 给定两个有序数组  正数k
# 求两个数累加和最大的前k个，两个数必须分别来自arr1 arr2
from typing import List
from unittest.runner import _ResultClassType

def get_max_two(arr1: List[int], arr2: List[int], K: int):
    result = []
    temp1, temp2 = len(arr1)-1, len(arr2)-1
    # result.append([arr1[temp1], arr2[temp2]])
    while K:
        result.append([arr1[temp1], arr2[temp2]])
        if temp1-1 and temp2 -1 and arr1[temp1-1] <= arr2[temp2-1]:
            temp2 = temp2 - 1
        elif temp1-1 and temp2 -1 and arr1[temp1-1] > arr2[temp2-1]:
            temp1 = temp1 -1
        else:
            break
        K = K - 1
    return result

# 一个数组 切成四块  累加和一样 切分位置不要
# 
# 
def can_cut(arr: List[int]):
    if not arr:
        return False
    n = len(arr)
    left, right = 0, n-1
    hash_map = {}
    sum = 0
    for i in range(len(arr)):
        hash_map[i] = sum
        sum += arr[i]
    #遍历的想法来
    #从1 位置开始枚举
    left_sum = arr[0]
    #找第二刀的位置是 left_sum + left_sum + arr[diyidao] 


# 判断是不是交错数组
def panduan(str1: str, str2: str, str3: str):
    # 小心 同一个字母 1 和2中都有 aaabc aa31 aaa3aab1c
    n1, n2, n3 = len(str1), len(str2), len(str3)
    if n1 + n2 != n3:
        return False
    dp = [[False] * (len(str2)+1) for _ in range(len(str1) + 1)]
    # 利用动态规划
    dp[0][0] = True
    for i in range(1, len(str2)+1):
        if dp[0][i-1] == False:
            break
        dp[0][i] = True if str2[i+1] == str3[i+1] else False
    for i in range(1, len(str1)+1):
        if dp[i-1][0] == False:
            break
        dp[i][0] = True if str1[i+1] == str3[i+1] else False
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str3[i+j-1] == str1[i-1] and dp[i-1][j]:
                dp[i][j] = True
            elif str3[i+j-1] == str2[j-1] and dp[i][j-1]:
                dp[i][j] = True
            else:
                dp[i][j] = False
    return dp[-1][-1]


# 排序最短子数组

def sorted(arr: List[int]):
    n = len(arr)
    left = -1
    right = len(arr)
    max_left = float("-inf")
    # 两次遍历 一次从左往右一次从右往左
    for i in range(len(arr)):
        if arr[i] > max_left:
            max_left = arr[i]
            continue
        else:
            left = i
    min_right = float("inf")
    for j in range(len(arr)-1, -1,-1):
        if arr[j] < min_right:
            min_right = arr[j]
            continue
        else:
            right = j
    return right - left + 1