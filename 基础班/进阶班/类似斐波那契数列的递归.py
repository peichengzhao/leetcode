#跳🐎问题

# def find_path_number(x: int, y: int, k: int, pos_x: int, pos_y: int):
#     return pocess(x, y, k)

# def pocess(x: int, y: int, k: int):
#     if k == 0:
#         return 1 if x==0 and y==0 else 0
#     #还有步数要走
#     if x < 0 or x > 9 or y < 0 or y > 8:
#         return 0
#     # 有步数要走  xy是棋盘上的位置
#     return pocess(x+2, y-1, k-1) + pocess(x-2, y+1 ,k-1) + pocess(x-1, y+2, k-1)



def process2(x: int, y: int, k: int):
    dp = [[[0 for _ in range(k+1)] for _ in range(9)] for _ in range(10)] # 10 9 3
    for i in range(10):
        for j in range(9):
            dp[i][j][0] = 0
    dp[0][0][0] = 1
    for level in range(1, k+1):
        for i in range(10):
            for j in range(9):
                dp[i][j][k] = dp[i+2][j-1][level-1] # 设计个函数去取值  因为可能有越界危险

    return dp[x][y][k]

def get_value(dp, x, y, k):
    if x < 0 or x > 9 or y < 0 or y > 8:
        return 0
    return dp[x][y][k]



# 一直往出吐球模型
import random
number1 = random.randint(1, 9)


from select import select
from typing import List

def sortArray(self, nums: list[int]) -> list[int]:
        # 快速排序核心函数
        def quick_sort(arr, left, right):
            # 递归终止条件：区间长度≤1，无需排序
            if left >= right:
                return
            # 优化1：随机选择基准值（避免有序数组导致的最坏时间复杂度O(n²)）
            pivot_idx = random.randint(left, right)
            # 将基准值交换到区间左端点，方便后续分区
            arr[left], arr[pivot_idx] = arr[pivot_idx], arr[left]
            
            # 分区操作：返回基准值的最终位置
            pivot_pos = partition(arr, left, right)
            
            # 递归排序基准值左侧和右侧的子数组
            quick_sort(arr, left, pivot_pos - 1)
            quick_sort(arr, pivot_pos + 1, right)
        
        # 分区函数：将数组分为「小于基准」和「大于基准」两部分，返回基准最终位置
        def partition(arr, left, right):
            pivot = arr[left]  # 基准值（已交换到左端点）
            # 双指针：i找大于基准的元素，j找小于基准的元素
            i, j = left, right
            while i < j:
                # 从右往左找第一个小于基准的元素
                while i < j and arr[j] >= pivot:
                    j -= 1
                # 从左往右找第一个大于基准的元素
                while i < j and arr[i] <= pivot:
                    i += 1
                # 交换这两个元素，让小于基准的到左边，大于的到右边
                arr[i], arr[j] = arr[j], arr[i]
            # 将基准值交换到最终位置（i=j的位置）
            arr[left], arr[i] = arr[i], arr[left]
            return i
        
        # 调用快速排序（左边界0，右边界len(nums)-1）
        quick_sort(nums, 0, len(nums) - 1)
        return nums












