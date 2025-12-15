from numpy import random


import os
import sys

def swap(list: list, i: int, j: int):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    return list

def translate_number(number: int):
    # 32位二进制数  左移 <<    右移 >>
    num = 32
    while(num >= 0):
        temp = 1 << num
        print("1" if number & temp else "0", end='')
        num -= 1

def calculate_N(number: int):
    # 1! + 2! + 3! + ... + n!
    final_result = 0
    temp_result = 1
    for i in range(1, number + 1):
        temp_result = temp_result * i
        final_result = final_result + temp_result
    return final_result


def paixu(list: list):
    if len(list) == 0 or len(list) == 1:
        return list

    max_index = len(list) - 1
    for i in range(0, max_index + 1):
        max_value = list[i]
        temp_num = i
        for j in range(i, max_index + 1 ):
            if list[j] < max_value:
                max_value = list[j]
                temp_num = j
        list[temp_num] = list[i]
        list[i] = max_value
    return list
def maopao(list: list):
    if len(list) == 0 or len(list) == 1:
        return list
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            if list[j] < list[j-1]:
                swap(list, j, j-1)
    return list

def xuanze(list:list):
    if len(list) == 0 or len(list) == 1:
        return list
    for i in range(0, len(list)):
        j = i
        while j > 0 and list[j-1] > list[j]:
            swap(list, j, j-1)
            j -= 1
    return list

#创建一个随机数组
def create_random_array(max_length: int, max_value: int):
    length = random.randint(1, max_length)
    list = []
    for i in range(length):
        list.append(random.randint(1, max_value))
    return list

# 验证数组是否有序
def is_sorted(list: list):
    max_value = list[0]
    for i in range(1, len(list)):
        if list[i] < max_value:
            return False
        max_value = list[i]
    return True
