from turtle import clear
from numpy import random


def static_double():
    test_time = 10000
    test_number = 0.3
    count = 0
    for i in range(test_time):
        # temp = max(random.random(), random.random())
        temp = min(random.random(), random.random())
        temp = 1 - temp
        if temp < test_number:
            count += 1
    return count / test_time

# 1-5 -> 1-7
def return_1_5():
    #return 1- 5
    temp = random.randint(1, 6)
    return temp

def return_0or1():
    temp = return_1_5()
    if temp == 3:
        return return_0or1()
    if temp == 1 or temp == 2:
        return 0
    else:
        return 1

def return_1_7():
    number_1 = 0
    number_2 = 0
    number_3 = 0
    for i in range(3):
        temp = return_0or1()
        if temp == 1 and i == 0:
            number_1 = 1
        if temp == 1 and i == 1:
            number_2 = 1
        if temp == 1 and i == 2:
            number_3 = 1
        if number_1 == 0 and number_2 == 0 and number_3 == 0:
            return return_1_7()
    return number_1 * 1 + number_2 * 2 + number_3 * 4

def return_000_111():
    temp = (return_0or1()<<2) + (return_0or1()<<1) + (return_0or1()<<0)
    return temp

def return_1_7_2():
    temp = (return_0or1()<<2) + (return_0or1()<<1) + (return_0or1()<<0)
    if temp == 0:
        return return_1_7_2()
    return temp

# 从01固定不等概率  -> 01等概率
def return_01_unequal_probability():
    temp =random.random()
    if temp < 0.3:
        return 0
    else:
        return 1
def return_01_equal_probability():
    temp = (return_01_unequal_probability()<<1) + return_01_unequal_probability()
    if temp == 0 or temp == 3:
        return return_01_equal_probability()
    elif temp ==1:
        return 0
    else:
        return 1


###====================================###



