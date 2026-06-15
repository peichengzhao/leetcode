# 假设一个固定窗口大小为w，依次划过arr
# 返回每一次滑出状况的最大值


from collections import deque

# def get_max_window(arr: list, w: int) -> list:
#     if not arr or w < 1 or len(arr) < w:
#         return []
#     help  = deque()
#     result = []
#     left, right = 0, 0
#     while right < len(arr):
#         while help is not None and arr[help.__getitem__(-1)] <= arr[right]:
#             help.pop()
#         help.append(right)
#         if right - left + 1 == w:
#             result.append(arr[help.popleft()])
#             left += 1
#             right += 1
#         else:
#             right += 1
#     return result
    

# def find_number(arr: list, num: int, w: int) -> int:
#     if not arr or len(arr) == 0:
#         return 0
#     max_deque = deque()
#     min_deque = deque()
#     left, right = 0, 0
#     reusult = 0
#     while right < len(arr):
#         while max_deque is not None and arr[max_deque.__getitem__(-1)] <= arr[right]:
#             max_deque.pop()
#         while min_deque is not None and arr[min_deque.__getitem__(-1)] >= arr[right]:
#             min_deque.pop()
#         max_deque.append(right)
#         min_deque.append(right)
#         if right - left + 1 == w:
#             if arr[max_deque.__getitem__(-1)] - arr[min_deque.__getitem__(-1)] <= num:
#                 result += 1
#             left += 1
#             right += 1
#         else:
#             right += 1
#     return result




# 单调栈
from collections import deque

def get_max_min_pos(arr: list) -> list:
    if not arr:
        return []
    help_stack = deque()
    result = []
    for i in range(len(arr)):
        while help_stack and arr[help_stack[-1]] > arr[i]:
            pop_idx = help_stack.pop()
            left_less = help_stack[-1] if help_stack else -1
            result.append([pop_idx, left_less, i])
        help_stack.append(i)
    while help_stack:
        pop_idx = help_stack.pop()
        left_less = help_stack[-1] if help_stack else -1
        result.append([pop_idx, left_less, -1])
    result.sort(key=lambda x: x[0])
    return result
    















