# N皇后问题

def main_n_queen(n_queen: int):
    if n_queen < 1:
        return 0
    record = [0] * n_queen
    return process(0, record, n_queen)

def process(index: int, record: list[int], n: int): # 有效行 是 0---n-1
    if index == n:
        return 1  #只有一种  上面的都摆好了
    #上面已经摆好了,考虑之后的拜访类型有多少种
    res = 0
    for j in range(n):
        if is_valid(record, index, j):
            record[index] = j
            res += process(index+1, record, n)
    return res

def is_valid(record: list[int], hang: int, lie: int):
    for i in range(hang):
        if record[i] == lie or abs(hang - i) == abs(lie - record[i]):
            return False
    return True


# N皇后问题 优化版本


def main_n_queen_optimize(n_queen: int):
    if n_queen < 1:
        return 0
    record = [0] * n_queen
    limit = (1 << n_queen) - 1 # 划定了问题的规模, 固定变量, 用位运算表示
# collim 列限制
# leftlim 左斜线限制
# rightlim 右斜线限制



def process_optimize(limit: int, collim: int, leftlim: int, rightlim: int):
    #只是加速了常数时间  时间复杂度仍是n^n
    if collim == limit:
        return 1 # 所有的列都摆满了
    pos = limit & (~(collim | leftlim | rightlim)) # 当前行可以摆放的位置
    # 当前行可以摆放的位置, 用位运算表示
    res = 0
    while pos != 0:
        most_right_one = pos & (~pos + 1)
        pos = pos - most_right_one
        res += process_optimize(limit, collim | most_right_one, (leftlim | most_right_one) << 1, (rightlim | most_right_one) >> 1)
    return res



#斐波那契数列

def main_fibonacci(n: int):
    if n < 1:
        return 0
    return process_fibonacci(n)

def process_fibonacci(n: int):
    if n == 1 or n == 2:
        return 1
    return process_fibonacci(n-1) + process_fibonacci(n-2)


#机器人走路问题
def robot_walk(N: int, M: int, K: int, P: int) -> int:
    if N < 2 or M < 1 or K < 1 or P < 1 or M > N or P > N:
        return 0
    return walk(N, M, K, P)

def walk(N: int, cur: int, rest: int, P: int) -> int:
    if rest == 0:
        return 1 if cur == P else 0
    if cur == 1:
        return walk(N, cur+1, rest-1, P)
    if cur == N:
        return walk(N, cur -1, rest -1, P)
    return walk(N, cur+1, rest-1, P) + walk(N, cur-1, rest-1, P)


def walk(N: int, cur: int, rest: int, P: int, dp: list[list[int]]) -> int:
    if dp[cur][rest] != -1:
        return dp[cur][rest]
    if rest == 0:
        dp[cur][rest] = 1 if cur == P else 0
        return dp[cur][rest]
    if cur == 1:
        dp[cur][rest] = walk(N, cur+1, rest-1, P, dp)
        return dp[cur][rest]
    if cur == N:
        dp[cur][rest] = walk(N, cur-1, rest-1, P, dp)
        return dp[cur][rest]
    dp[cur][rest] = walk(N, cur+1, rest-1, P, dp) + walk(N, cur-1, rest-1, P, dp)
    return dp[cur][rest]
