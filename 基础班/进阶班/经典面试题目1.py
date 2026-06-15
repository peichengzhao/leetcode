#给一个arr有序   给一个K K 是绳子长度  看看能覆盖多长

from typing import List

def get_max_point(arr: List[int], K: int):
    if not arr or K <= 0:
        return 0
    begin, end = 0, K
    number = 0
    max_number = 0
    for i in range(len(arr)):
        number = 1
        for j in range(i+1,len(arr)):
            if arr[j] - arr[i] <=K:
                number += 1
                max_number = max(number, max_number)
    return max_number



def get_max_point(arr: List[int], K: int):
    if not arr or K <= 0:
        return 0
    left, right = 0, 0 
    N = len(arr)
    hash_map = {}
    max_point = 0
    while (right < len(arr)):
        while (right < len(arr) and arr[right] - arr[left] <= K):
            right += 1
        max_point = max(max_point, right-left)
        left += 1
    return max_point
#怎么判断一个括号字符串有效？  如果一个括号字符串无效  至少填写一个字符能让其有效  只有()()()()()


def number_kuohao(strr: str):
    if not strr:
        return False, 0
    if len(strr) == 1:
        return False, 1
    count, need = 0, 0
    for i in range(len(strr)):
        if strr[i] == "(":
            count +=1
        else:
            count -=1
        if count == -1:
            need += 1
            count = 0 
    if need == 0 and count == 0 :
        return True
    if count != 0 or need != 0:
        return count + need
    return True



# 找出最长有效字串
def max_length(strr: str):
    if not strr:
        return 0
    dp = [0] * len(strr)
    dp[0] = 0
    ans = 0
    for i in range(len(strr)):
        if strr[i] == "(":
            dp[i] == 0
        else:
            pre_length = dp[i-1]
            pre = i - 1 - pre_length
            if pre>=0 and strr[pre] == "(":
                dp[i] = pre_length + 2 + (dp[pre-1] if pre >0 else 0)
            elif pre>=0 and strr[pre] == ")":
                dp [i] = pre_length + 2
        ans = max(ans, dp[i])
    return ans


# s = RGRGR -> RRRGG  确保每一个R都比G 靠最左边近    每一个点都可以使用RG 染色

def change(s: str):
    if not s or len(s) == 0:
        return
    # 枚举分界线
    temp = -1
    min_number = 0
    while temp < len(s) - 1:
        left = temp
        right = temp + 1
        left_number = 0
        right_number = 0
        while left >=0:
            if s[left] == "G":
                left_number += 1
        while right <= len(s) -1:
            if s[right] == "R":
                right_number += 1
        min_number = min(min_number, left_number + right_number)
        temp += 1
    return min_number
        

def change(s: str):
    if not s or len(s) == 0:
        return
    # 枚举分界线
    # 右侧上关心几个R 右侧关心几个G
    left_G = []
    left_number = 0
    for i in range(len(s)):
        if s[i] == "G":
            left_number += 1
        left_G.append(left_number)
    right_R = []
    right_number = 0
    for j in range(len(s)-1, -1 ,-1):
        if s[j] == "R":
            right_number += 1
        right_R.append(right_number)
    min_number = float('inf')
    for k in range(len(s)):
        left_temp = left_G[k]
        right_temp = right_R[k+1] if k+1 <len(s) else 0
        min_number = min(left_temp+right_temp, min_number)
    return min_number
# 矩阵都是10 N*N  边框都是1 的正方形 最大边长

def get_max_length(matrix: List[List[int]]):
    if not matrix:
        return 0
    # r[i][j] 右方有多少1
    # d[i][j] 下方有多少1
    r = [0 for _ in range(len(matrix))] * len(matrix)
    d = [0 for _ in range(len(matrix))] * len(matrix)
    for i in range(len(matrix) - 1, -1, -1):
        d[i][len(matrix) - 1] = 1
    for i in range(len(matrix) - 1, -1, -1):
        r[len(matrix) - 1][i] = 1
    for i in range(len(matrix)-2, -1, 0):
        for j in range(len(matrix) - 1):
            if matrix == "0":
                d[i][j] = 0
            else:
                d[i][j] = d[i+1][j] + 1
    for i in range(len(matrix)-2, -1, 0):
        for j in range(len(matrix) - 1):
            if matrix[j][i] == "0":
                d[j][i] = 0
            else:
                d[j][i] = d[j][i+1] + 1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            length = min(len(matrix)-i ,len(matrix)-j)
            for k in range(length):
                if d[i][j]>= k and r[i][j] >= k:
                    max_length = max(max_length, k)
    return max_length
















