# 快速排序

# def quick_sort(list: list):
#     return partition(list)

# def partition(list: list):
#     member = list[len(list)-1]
#     less = -1
#     index = 0
#     for i in range(len(list)-1):
#         if list[index] < member:
#             change(list, index, less+1)
#             less += 1
#         index += 1
#     change(list, less+1, len(list)-1)

def change(list:list, i:int, j:int):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    return



def quick_sort(list: list):
    if len(list) < 2:
        return list
    return partition(list)

def partition(list: list):
    member = list[len(list-1)] 
    less = -1
    more = len(list)
    for i in range(len(list)-1):
        if list[i] < member:
            less += 1
            change(list, less, i)
            i += 1
        if list[i] > member:
            more -= 1
            change(list, more, i)
        if list[i] == member:
            i += 1
        if i == more:
            break
    return list


def partition_2(list: list, left: int, right: int):
    if left == right:
        return left
    member = list[(left + right) // 2]
    less = left - 1
    more = right + 1
    index = left
    while index < more:
        if list[index] ==member:
            index += 1
        elif list[index] < member:
            less += 1
            change(list, less, index)
            index += 1
        elif list[index] > member:
            more -= 1
            change(list, more, index)
    partition_2(list, left, less)
    partition_2(list, more, right)
    return

def quick_sort_2(list: list):
    if len(list) < 2:
        return list
    return partition_2(list, 0, len(list)-1)

def change(list:list, i:int, j:int):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    return



def quick_sort_3(list: list):
    