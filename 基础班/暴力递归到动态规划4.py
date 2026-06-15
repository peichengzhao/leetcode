# 给定一个字符串str,给定一个字符串类型的数组arr

# 判断str是否能被arr中的字符串拼接出来
# 例如：str = "leetcode", arr = ["leet", "code"] return True
# 例如：str = "leetcode", arr = ["leet", "cod"] return False



def main(str: str, arr: list[str]):
    length = len(arr)
    map = [[0] * 26 for _ in range(length)]
    for i in range(length):
        for j in range(len(arr[i])):
            map[i][ord(arr[i][j]) - ord('a')] += 1
    dp = {}
    dp[""] = 0
    return process(str, map, dp)


def process(rest: str, map: list[list[int]], dp: dict):
    if rest in dp:
        return dp[rest]
    min_number = float('inf')
    number = len(map)
    target = [0] * 26
    for i in range(len(rest)):
        target[ord(rest[i]) - ord('a')] += 1
    # map 区搞定target
    for i in range(number):
        if map[i][target[0] - 'a'] > 0:
            new_rest = rest.replace(map[i], "")
            continue
    



# 两个字符串 最长公共子序列

def main_2(str1: str, str2: str):
    dp = [[0] *len(str2) for _ in range(len(str1))]
    first = False
    for i in range(len(str2)):
        dp[i][0] = max(dp[i-1][0], 1 if str1[0] == str2[i] else 0)
        # if str1[0] == str2[i]:
        #     first = True
        # if first:
        #     dp[0][i] = 1
    second = False
    for i in range(len(str1)):
        if str[0] == str2[0]:
            second = True
        if second:
            dp[i][0] = 1
    #最长公共子序列
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if str1[i] == str2[j]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
    return dp[len(str1)-1][len(str2)-1]
    


# 咖啡机喝咖啡问题
def main_3(arr: list[int], a: int, b: int):
    # a 代表咖啡机洗一杯咖啡的时间
    # b 代表杯子自由挥发的时间
    return process_3(arr, a, b, 0, 0)




 # 假设index之前的杯子都洗完了，index号杯子决定洗还是挥发
def process_3(drinks: list[int], a: int, b: int, index: int, washline: int):
    if index == len(drinks):
        return min(max(washline, drinks[index]) + a, drinks[index] + b) # 洗或者挥发
    #决定用机器
    wash = max(washline, drinks[index]) + a
    next1 = process_3(drinks, a, b, index+1, wash)
    #决定挥发
    wash2 = max(washline, drinks[index]) + b
    next2 = process_3(drinks, a, b, index+1, wash2)
    return min(next1, next2)


def dp(drinks: list[int], a: int, b: int):
    length = len(drinks)
    limit = 0
    if a >= b:
        return drinks[-1] + b
    #认为a<b
    for i in range(length):
        limit = max(limit, drinks[i]) + a
    #定义了极限
    dp = [[0] * (limit + 1) for _ in range(length)]
    for watchline in range(limit + 1):
        dp[n-1]




















