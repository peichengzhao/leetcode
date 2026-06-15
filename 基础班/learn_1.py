# 不借助第三个变量，交换两个变量的值

# 利用异或运算

def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

test = [1, 2, 3, 5, 6]

def swap(list: list, i: int, j: int):
    list[i] = list[i] ^ list[j]
    list[j] = list[i] ^ list[j]
    list[i] = list[i] ^ list[j]
    return list

def find(list: list):
    if len(list) == 0 or list == None:
        return -1
    eor = 0 ^ list[0]
    for i in range(1, len(list)):
        eor = eor ^ list[i]
    return eor


def find_2(list: list):
    if len(list) == 0 or list == None:
        return -1, -1
    eor = 0 ^ list[0]
    for i in range(1, len(list)):
        eor = eor ^ list[i]
    idx = 1
    while(idx < eor and idx^eor == 0):
        idx = idx << 1
    eor1 = 0
    eor2 = 0
    list_1 = []
    list_2 = []
    for i in range(0, len(list)):
        if list[i] ^ idx != 0:
            list_1.append(list[i])
        else:
            list_2.append(list[i])
    for i in range(0, len(list_1)):
        eor1 = eor1 ^ list_1[i]
    for i in range(0, len(list_2)):
        eor2 = eor2 ^ list_2[i]
    return eor1, eor2



def number(number: int):
    count = 0
    while (number != 0):
        right_one = number & (~number + 1)
        count += 1
        number = number ^ right_one
    return count



