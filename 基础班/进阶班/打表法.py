# 小虎去买苹果   两种类型的塑料袋 任意数量
# 
# 1： 6  2： 7
# 使用袋子尽量少  且使用的袋子装满
# 
# 如果无法满足 则不买 返回-1
# 
# 
# 
# 
def buy_apple(N: int):
    if N < 6:
        return -1
    # 奇数无法被分解
    if N % 2 == 1:
        return -1
    number_8 = N // 8
    for number in range(number_8, -1 ,-1):
        rest_apple_number = N - (number * 8)
        if rest_apple_number >= 0:
            if rest_apple_number % 6 == 0:
                return number + rest_apple_number // 6
    return -1


# for i in range(30):
#     print(f"{i} : {buy_apple(i)}")





def buy_apple_1(N : int):
    if N % 2 == 1:
        return -1
    if N <= 18:
        if N == 6 or N == 8:
            return 1
        if N == 12 or N == 14 or N == 16:
            return 2
        else:
            return -1
    return (N - 18) / 8 + 3

#找出来规律
 # 打表找规律


#给N N份青草  一只牛 一只羊 轮流吃  1， 4， 16， 64>... 假设牛羊都特别聪明 返回谁会赢  谁把草吃完 谁赢  牛先吃

def who_win(N :int):
    if N == 0 :
        return "先手"
    if N < 5:
        return "后手" if N == 2 else "先手"
    base = 1
    while base <= N:
        if (who_win(N - base) == "后手"):
            return "先手"
        if base * 4 > N:
            break
        base *= 4
    return "后手"
    






def is_ok(number: int):
    if number < 3:
        return False
    for i in range(number):
        sum = 0
        for k in range(i, number):
            sum += k
            if sum == number:
                return True
            if sum > number:
                break
    return False







def is_ok_2(number: int):
    if number < 3:
        return False
    if number >= 3:
        return False if (number & (number - 1)) != 0 else True

# for i in range(100):
#     print(f"{i}  : {is_ok_2(i)}")



# zigzag打印矩阵

from typing import List


# def print(arr: [List[int]], A: [int, int], B: [int, int], from_up : bool):

# def print_zigzag(arr: [List[int]]):
#     Ar, Ac, Br, Bc = 0, 0, 0, 0
#     endr = len(arr) - 1
#     endc = len(arr[0]) - 1
#     from_up = False
#     while (Ar != endr + 1):
#         print(arr, Ar, Ac, Br, Bc, from_up)
#         Ar = Ar+1 if Ac == endc else Ar
#         Ac = Ac+1 if Ac == endc else Ac
#         Bc = Bc+1 if Bc == endc else Bc
#         Br = Br+1 if Br == endc else Br
#         from_up = not from_up


# def print(arr: [List[int]], Ar: int, Ac: int, Br: int, Bc: int, from_up : bool):





#转圈儿打印矩阵

def print_arr(arr: List[List[int]]):
    up, down, left, right = 0, len(arr) - 1, 0, len(arr[0]) - 1
    while up <= down and left <= right:
        for j in range(left, right+1):
            print(arr[up][j])
        up += 1
        if up > down:
            break
        for i in range(up, down+1):
            print(arr[i][right])
        right -= 1
        if right < left:
            break
        for j in range(right, left-1, -1):
            print(arr[down][j])
        down -= 1
        if up > down:
            break
        for i in range(down, up-1, -1):
            print(arr[i][left])
        left += 1
    return 


#原地旋转正方形矩阵

def fenquan(arr: List[List[int]], left: int, right: int):
    for k in range(right-left):
        temp = arr[left][left+k]
        arr[left][left+k] = arr[right-k][left]
        arr[right-k][left] = arr[right][right-k]
        arr[right][right-k] = arr[left+k][right]
        arr[left+k][right] = temp


def xuanzhuan_arr(arr: List[List[int]]):
    left, right = 0, len(arr) - 1
    #一层一层
    while left <= right:
        fenquan(arr, left, right)
        left += 1
        right -= 1
    return 

    
        