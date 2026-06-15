
def bag_problem(weights: list[int], values: list[int], bag: int):
    results = []
    max_value = process5(weights, values, 0, 0, 0, results, bag)
    return max_value

def process5(weights: list[int], values: list[int], index: int, already_weight: int, already_value: int, results: list[int], bag: int):
    if already_weight > bag:
        return -1 # 无效解
    if index == len(weights):
        return 0 # 方案有效
    p1 = process5(weights, values, index+1, already_weight, already_value, results, bag) # 不选当前物品
    p2 = process5(weights, values, index+1, already_weight+weights[index], already_value+values[index], results, bag) # 选当前物品
    return max(p1, p2)

def process6(weights: list[int], values: list[int], index: int, rest_weight: int):
    # 修复问题3：剩余承重不足，返回0（无收益），而不是-1
    if rest_weight <= 0:
        return -1
    # 递归终止条件：遍历完所有物品，无收益，返回0（你的代码这行完全正确）
    if index == len(weights):
        return 0
    
    # 分支1：不选第index个物品，直接去下一个物品，剩余承重不变
    pi = process6(weights, values, index+1, rest_weight)
    
    # 分支2：选第index个物品（新增超重校验+修复核心逻辑：累加价值）
    pi2 = -1 # 默认不选
    p2_next = process6(weights, values, index+1, rest_weight - weights[index])
    if p2_next != -1:
        pi2 = values[index] + p2_next
    # 两种选择取最大价值，返回最优解
    return max(pi, pi2)


def bag_problem_dp(weights: list[int], values: list[int], bag: int):
    dp = [[-1] * (bag + 1) for _ in range(len(weights) + 1)]
    for i in range(len(weights) + 1):
        dp[i][0] = 0
    for j in range(bag + 1):
        dp[0][j] = 0
    for i in range(1, len(weights) + 1):
        for j in range(1, bag + 1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
    return dp[len(weights)][bag]


def main(arr: []):
    if len(arr) == 0:
        return 0
    length = len(arr)
    dp_f = [[-1] * length for _ in range(length)]
    dp_s = [[-1] * length for _ in range(length)]
    for i in range(length):
        dp_f[i][i] = arr[i]
        dp_s[i][i] = 0
    for i in range(1, length):
        hang = 0 
        lie = i
        while hang < lie and lie < length:
            dp_f[hang][lie] = max(arr[hang] + dp_s[hang+1][lie], arr[lie] + dp_s[hang][lie-1])
            dp_s[hang][lie] = min(dp_f[hang+1][lie], dp_f[hang][lie-1])
            hang += 1
            lie += 1
    return dp_f[0][length-1]


def huobimianzhi(arr: list[int] , aim: int):
    if len(arr) == 0:
        return 0
    return process(arr, 0, aim)


def process(arr: list[int], index: int, rest: int):
    if rest < 0:
        return 0
    if index == len(arr):
        return 1 if rest == 0 else 0
    #使用当前货币
    number = 1
    sum_number = 0
    while number * arr[index] <= rest:
        p1_sum = process(arr, index+1, rest-(arr[index]*number))
        sum_number += p1_sum
        number += 1
    p2_sum = process(arr, index+1, rest)
    sum_number += p2_sum
    return sum_number


def huobimianzhi_dp(arr: list[int] , aim: int):
    if len(arr) == 0:
        return 0
    length = len(arr)
    hasp_map = {}


def process_dp(arr: list[int], index: int, rest: int, hasp_map: dict):
    if rest < 0:
        return 0
    if index == len(arr):
        return 1 if rest == 0 else 0
    #使用当前货币
    number = 0
    sum_number = 0
    while number * arr[index] <= rest:
        if (index, rest-(arr[index]*number)) in hasp_map:
            p1_sum = hasp_map[(index, rest-(arr[index]*number))]
        else:
            p1_sum = process(arr, index+1, rest-(arr[index]*number))
            hasp_map[(index, rest-(arr[index]*number))] = p1_sum
        sum_number += p1_sum
        number += 1
    return sum_number

def process_dp_2(arr: list[int], aim: int):
    if len(arr) == 0:
        return 0
    length = len(arr)
    dp = [[-1] * (aim + 1) for _ in range(length + 1)]
    for i in range(length + 1):
        dp[i][0] = 1
    for j in range(aim + 1):
        dp[0][j] = 0
    for i in range(1, length + 1):
        for j in range(1, aim + 1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:










