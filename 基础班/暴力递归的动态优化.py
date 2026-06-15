# 暴力递归的动态优化

# 1. 记忆化搜索
# 2. 动态规划
# 3. 分治法
# 4. 贪心算法
# 5. 回溯法
# 6. 分支限界法
# 7. 模拟退火算法
# 8. 遗传算法
# 9. 蚁群算法
# 10. 粒子群算法
# 打印所有的子序列


from unittest import TextTestRunner


def print_all_subsequences(strs: str):
    if  len(strs) == 0:
        return []
    results = []
    process(strs, 0, "", results)
    return results

def process(strs: str, index: int, path: str, results:list[str]):
    if index == len(strs):
        results.append(path)
        return  # 出口
    #不要当前字符
    new_path = path
    process(strs, index+1 ,new_path, results)
    # process(strs, index+1, path, results)
    #要当前字符
    new_path_1 = path + strs[index]
    process(strs, index+1, new_path_1, results)
    # process(strs, index+1, path+strs[index], results)
    return
# 打印所有的子序列, 不出现重复字面值的子序列

def print_all_subsequences_no_repeat(strs: str):
    if len(strs) == 0:
        return []
    results = {}
    process_no_repeat(strs, 0, "", results)
    return list(results.keys())

def process_no_repeat(strs: str, index:int, path:str, results: dict):
    if index == len(strs):
        results[path] = True
        return 
    #不要当前节点
    process_no_repeat(strs, index+1, path, results)
    #要当前节点
    process_no_repeat(strs, index+1, path+strs[index], results)
    return

def swap(arr:list, i:int, j:int):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

#字符的全排列

def print_all_permutations(strs: str):
    if len(strs) == 0:
        return []

def process_permutations(strs: str, index:int, results: list[str]):
    if index == len(strs):
        results.append(strs)
        return
    for i in range(index, len(strs)): # i 就在尝试index后面的位置 所有位置
        swap(strs, index, i)
        process_permutations(strs, index+1, results)
        swap(strs, index, i) # 恢复现场
    return


# 分支限界法

def process_branch_and_bound(strs: str, index:int, results: list[str]):
    if index == len(strs):
        results.append(strs)
        return
    visited = [False] * 26
    for i in range(index, len(strs)):
        if visited[ord(strs[i]) - ord('a')]:
            continue
        visited[ord(strs[i]) - ord('a')] = True
        swap(strs, index, i)
        process_branch_and_bound(strs, index+1, results)
        swap(strs, index, i)
        visited[ord(strs[i]) - ord('a')] = False
    return



# A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8, I=9, J=10, K=11, L=12, M=13, N=14, O=15, P=16, Q=17, R=18, S=19, T=20, U=21, V=22, W=23, X=24, Y=25, Z=26
# 给定一个数字字符串，求有多少种字母组合方式
# 111 -> AAA, KA, AK


# bag, value
# 给定一个背包容量，给定一个物品重量，给定一个物品价值，求背包能装下的最大价值
# 背包问题

def find_max_value(weights: list[int], values: list[int], bag_value: int):
    if len(weights) == 0 or len(values) == 0 or bag_value <= 0:
        return 0
    results = []
    process_find_max(weights, values, 0, bag_value, results)
    return max(results)


def process_find_max(weights: list[int], values: list[int], index:int, rest_weight:int, results: list[int]):
    if rest_weight < 0:
        return -1 # 如果返回-1 说明无效解
    if index == len(weights):
        return 0
    #不选当前货物
    p1 = process_find_max(weights, values, index+1, rest_weight, results)
    #选当前货物
    p2_next = process_find_max(weights, values, index+1, rest_weight-weights[index], results)
    p2 = -1
    if p2_next != -1:
        p2 = p2_next + values[index]

    return max(p1, p2)

















