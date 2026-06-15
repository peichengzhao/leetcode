# 给arr ["b\st", "d\", "a\d\e", "a\b\c"]
# 打印出来目录结构

from typing import List

from numpy import sort

#给了先序和 中序 返回后续


def get_hou(arr_pre: List[int], arr_in: List[int]):
    if not arr_pre or arr_in:
        return 
    
def process(arr_pre: List[int], pre_begin: int, pre_end: int, arr_in: List[int], in_begin: int, in_end: int, result: List[int], res_beign: int, res_end: int):
    if pre_begin > pre_end or in_begin > in_end:
        return
    result[res_end] = arr_pre[pre_begin]
    middle = in_begin
    for j in range(in_begin, in_end+1):
       if arr_in[j] == arr_pre[pre_begin]:
        middle = j
        break
    #处理左树  
    process(arr_pre, pre_begin - 1, pre_begin + middle - in_begin, arr_in, in_begin, middle - 1, result, res_beign , res_beign + middle - 1)
    #右边的树
    process(arr_pre, pre_end - middle + in_begin + 1, pre_end, arr_in, middle + 1, in_end, result, res_beign + middle, res_end - 1)
    return 

#两个字符串 求最长公共子序列


def get_max(str_1: str, str_2: str):
    
    if not str_1 or not str_2:
        return 0
    
    def process(str_1: str, str_2: str, index_1: int, index_2: int):
        if index_1 == 0 and index_2 == 0:
            return 1 if str_1[index_1] == str_2[index_2] else 0
        if index_1 == 0:
            return 1 if process(str_1, str_2, index_1, index_2-1) else 0
        if index_2 == 0:
            return 1 if process(str_1, str_2, index_1-1, index_2) else 0
        p1 = process(str_1, str_2, index_1-1, index_2-1)
        p2 = process(str_1, str_2, index_1, index_2-1)
        p3 = process(str_1, str_2, index_1-1, index_2)
        p4 = p1 + 1 if str_1[index_1] == str_2[index_2] else -1
        return max(max(p1, p2), max(p3, p4))
    return process(str_1, str_2, len(str_1)-1, len(str_2)-1)

# 使用前缀树
test = "a\\b\\c"
print(test)
arr = test.split("\\")
print(arr)




#信封问题
def xinfengwenti(arr: List[List[int]]):
    if not arr:
        return None
    sorted_arr = sorted(arr, key=lambda x: x[1])
    sorted_arr = sorted(arr, key=lambda x: x[0])
    help_arr = []
    for i in range(sorted_arr):
        help_arr.append(i[1])
    # 观察最长递增子序列 返回结果
    
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            litele = i
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    litele = j
                    break
            dp[i] = dp[litele] + 1 if litele != i else 1
        max_length = 1
        for k in range(len(dp)):
            if dp[k] > max_length:
                max_length = dp[k]
        return max_length
