#哈希表
#快速排序、归并排序、随机快排


def quick_sort(list: list):
    if len(list) < 2:
        return list
    return process(list, 0, len(list)-1)

def process(list:list, left:int, right:int):
    if left == right:
        return
    min = (left + right) // 2
    process(list, left, min)
    process(list, min+1, right)
    merge(list, left, min, min+1, right)
    return list

def merge(list:list, left_1:int, right_1:int, left_2:int, right_2:int):
    help = []
    i, j = left_1, left_2
    while i<=right_1 and j < right_2:
        if list[i] < list[j]:
            help.append(list[i])
            i += 1
        else:
            help.append(list[j])
            j += 1
    while i <= right_1:
        help.appendp(list[i])
        i += 1
    while j <= right_2:
        help.append(list[j])
        j += 1
    for k in range(len(help)):
        list[left_1 + k] = help[k]
    return 


#非递归版本
def quick_sort(list: list):
    if len(list) < 2:
        return list
    merge_size = 1
    while merge_size < len(list):
        left = 0
        while left < len(list):
            mid = left + merge_size - 1
            right = left + 2*merge_size - 1
            if right < len(list):
                merge(list, left, mid, right, right + merge_size - 1)
            elif mid < len(list):
                merge(list, left, mid, mid, len(list) - 1)
            left = left + 2*merge_size
        merge_size = merge_size * 2
    return list


    