# 二分法
# 在一个有序数组中，找某个数是否存在
from dis import hasname
from numpy import random

def find_number_in_sorted_array(list: list, number:int) -> bool:
    if len(list) ==0 or list == None:
        return False
    left = 0
    right = len(list) - 1
    mid = (left + right) // 2
    while(left <= right):
        mid = (left + right) // 2
        if list[mid] == number:
            return True
        if list[mid]< number:
            left = mid + 1
        else:
            right = mid - 1
    return False

def most_left_nomorennum(list: list, number:int) -> int:
    # 最左的 不小于number的位置
    if len(list) ==0 or list == None:
        return -1
    left = 0
    right = len(list) - 1
    temp = -1
    while(left <= right):
        # updata temp
        mid = (left + right) // 2
        if list[mid] >= number:
            temp = mid
            right = mid -1
        else:
            left = mid + 1
    return temp

#局部最小值
# 有一个数组无序，任意两个相邻的数不相等
# 局部最小： 0位置比1小，n-1位置比n-2小，i位置比i-1和i+1小
# 返回任意一个局部最小位置
def local_minimum(list:list) -> int:
    length = len(list)
    if length == 1:
        return 0
    if len(list) ==0 or list == None:
        return -1
    if list[0] < list[1]:
        return 0
    if list[length-1] < list[length-2]:
        return length-1
    left = 0
    right = length-1
    mid = (left + right) // 2
    while(left <= right):
        mid = (left + right) // 2
        if list[mid] < list[mid-1] and list[mid] < list[mid+1]:
            return mid
        if list[mid] > list[mid-1]:
            right = mid - 1 
        else:
            left = mid + 1
    return -1

def create_random_array(max_length: int, max_value: int):
    length = random.randint(1, max_length)
    list = []
    list.append(random.randint(1, max_value))
    for i in range(1, length-1):
        temp = random.randint(1, max_value)
        while temp == list[i-1]:
            temp = random.randint(1, max_value)
        list.append(temp)
    return list

# 时间复杂度
#核心是字典
hash_dict = {"name": "Alice", "age": 20}  
hash_dict["gender"] = "female" # 增加
hash_dict["age"] = 21 # 修改
del hash_dict["age"] # 删除
hash_dict["xingge"] = "xxi" # 增加

#有序表
from collections import OrderedDict

# 创建有序字典
ordered_dict = OrderedDict([("a", 21), ("b", 67), ("c", 100)])
for i, j in ordered_dict.items():
    print(i, j)

ordered_dict.move_to_end('b', last=False)
ordered_dict.pop('a')

