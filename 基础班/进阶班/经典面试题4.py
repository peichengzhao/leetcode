class Job:
    money : int
    hard: int

from typing import List


def bag_problem(eat: List[int], w: int):
    return process(eat, w, 0, w)
    #多少种方案

def process(eat: List[int], w: int, index: int, rest: int):
    if rest < 0:
        return 0
    if index == len(eat):
        return 1
    slove_1 = process(eat, w, index+1, rest-eat[index])
    slove_2 = process(eat, w, index+1, rest)
    return slove_2 + slove_1

def bag_problem(eat: List[int], w: int) -> int:
    # 边界处理：无物品或容量为0
    if not eat or w < 0:
        return 0
    
    n = len(eat)  # 物品数量
    # 正确初始化dp数组：dp[容量][物品索引]，全0二维数组（避免内存共享）
    # 行：容量0~w（共w+1行），列：物品0~n-1（共n列），额外多一列n作为终止条件
    dp = [[0] * (n + 1) for _ in range(w + 1)]
    
    # 初始化：当处理完所有物品（i=n）且容量为0时，组合数为1（空集）
    for j in range(w + 1):
        dp[j][n] = 1 if j == 0 else 0
    
    # 逆序遍历物品（从最后一个物品往前）
    for i in range(n - 1, -1, -1):
        # 遍历所有容量
        for j in range(w + 1):
            # 不选当前物品：继承下一个物品的组合数
            dp[j][i] = dp[j][i + 1]
            # 选当前物品：若容量足够，加上选当前物品后的组合数
            if j >= eat[i]:
                dp[j][i] += dp[j - eat[i]][i + 1]
    
    return dp[w][0]



#二维数组


#最长公共子串

def get_together(str_1: str, str_2: str):
    # 一个做行 一个做列
    dp = [[0] * (len(str_1)) for _ in range(len(str_2))]
    max_value = 0
    for i in range(str_1):
        if str_2[0] == str_1[i]:
            dp[0][i] = 1
            max_value = 1
        else:
            dp[0][i] = 1
    for i in range(str_2):
        if str_1[0] == str_2[i]:
            dp[i][0] = 1
            max_value = 1
        else:
            dp[i][0] = 1
    for j in range(1, len(str_1)):
        for i in range(str_2):
            if str_1[j] == str_2[i]:
                dp[i][j] = dp[i-1][j-1]
                max_value = max(max_value, dp[i][j])
            else:
                dp[i][j] = 0
    return max_value


def get_together(str_1: str, str_2: str):
    # 一个做行 一个做列
    help_list = [0] * len(str_1)
    max_value = 0



def find_most_str(strs: List[str]):
    if not strs:
        return None
    
            
    
    


















