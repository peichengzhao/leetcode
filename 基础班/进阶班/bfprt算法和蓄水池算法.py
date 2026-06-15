# #字符串匹配问题

# def match(str1: str, match: str):
#     if not str1 or not match:
#         return -1
#     if len(str1) < len(match):
#         return -1
#     for i in range(len(str1) - len(match) + 1):
#         if str1[i:i+len(match)] == match:
#             return i
#     return -1 

# def match_kmp(str1: str, match :str):
#     if not str1 or not match:
#         return -1
#     if len(str1) < len(match):
#         return -1
#     i, j = 0, 0
#     next_array = get_next_array(match)
#     while i < len(str1) and j < len(match):
#         if str1[i] == match[j]:
#             i += 1
#             j += 1
#         elif j == 0:
#             i += 1
#         else:
#             j = next_array[j]
#     return i - j if j == len(match) else -1

# # def get_next_array(match: str):
# #     if not match:
# #         return []
# #     next_array = [0] * len(match)
# #     next_array[0] = -1
# #     next_array[1] = 0
# #     for i in range(2, len(match)):
# #         cur = i - 1
# #         while cur >= 0 and match[i-1] != match[next_array[cur]]:
# #             cur = next_array[cur]
# #         if cur < 0:
# #             next_array[i] = 0
# #         else:
# #             next_array[i] = next_array[cur] + 1
# #     return next_array

# def get_next_array(match: str):
#     if not match:
#         return []
#     if len(match) == 1:
#         return [-1]
#     if len(match) == 2:
#         return [-1, 0]
#     next = [0] * len(match)
#     next[0], next[1] = -1, 0
#     i, j = 2, 0
#     while i < len(match):
#         if match[i - 1] == match[j]:
#             next[i] = j + 1
#             i += 1
#             j += 1
#         elif j > 0:
#             j = next[j]
#         else:
#             next[i] = 0
#             i += 1
#     return next


# #暴力解
# def find_postion(strr: str, match: str):
#     if not strr or not match:
#         return -1
#     if len(match) > len(strr):
#         return -1
#     for i in range(len(strr)):
#         temp = 0
#         while strr[i+temp] == match[temp] and temp < len(match) and i+temp < len(strr):
#             temp += 1
#         if temp != len(match):
#             temp = 0
#         elif temp==len(match):
#             return i
#         else:
#             return -1
#     return -1


# #利用next数组

def build_nextval(match: str):
    if not match or len(match) == 0:
        return []
    if len(match) == 1:
        return [-1]
    if len(match) == 2:
        return [-1, 0]
    i, j = 2, 0
    nextval = [-1] * len(match)
    nextval[1] = 0
    while i < len(match):
        if match[i-1] == match[j]:
            nextval[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = nextval[j]
        else:
            nextval[i] = 0
            i += 1
    return nextval 
        

def find_sub_str(str_1: str, str_2:str):
    if not str_1 or not str_2 or len(str_2) > len(str_1):
        return -1
    next_val_list = build_nextval(str_2)
    i, j = 0, 0
    while i < len(str_1) and j < len(str_2):
        if str_1[i] == str_2[j]:
            i += 1
            j += 1
        elif j > 0:
            j = next_val_list[j]
        else:
            i += 1
    return i - j if j == len(str_2) else -1



print(find_sub_str("hello world", "python"))
















