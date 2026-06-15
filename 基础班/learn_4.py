# 在一个数组当中  一个数左边比它小的数的累加和d
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
        help.append(list[i])
        i += 1
    while j <= right_2:
        help.append(list[j])
        j += 1
    for k in range(len(help)):
        list[left_1 + k] = help[k]
    return 

def small_sum(list: list):
    if len(list) ==0 or list == None:
        return 0
    sum = 0
    process(list, 0 ,len(list)-1, sum)
    return sum

def process(list: list, left: int, right:int, sum: int):
    if left == right:
        return
    mid = (left + right) // 2
    index = left
    while index <= mid:
        temp = 0
        for i in range(mid+1, right+1):
            if list[index] < list[i]:
                temp += 1
            if list[index] >= list[i]:
                break
        sum += temp * list[index]
        index += 1
    process(list, left, mid, sum)
    process(list, mid+1, right, sum)
    merge(list, left, mid, mid+1, right)
    return


class SamllSum:
    def __init__(self):
        self.sum =0
    def merge(self, list:list, left_1:int, right_1:int, left_2:int, right_2:int):
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
            help.append(list[i])
            i += 1
        while j <= right_2:
            help.append(list[j])
            j += 1
        for k in range(len(help)):
            list[left_1 + k] = help[k]
        return 

    def small_sum(self, list: list):
        if len(list) ==0 or list == None:
            return 0
        self.process(list, 0 ,len(list)-1)
        return self.sum

    def process(self, list: list, left: int, right:int,):
        if left == right:
            return
        mid = (left + right) // 2
        self.process(list, left, mid)
        self.process(list, mid+1, right)
        index = left
        while index <= mid:
            temp = 0
            for i in range(mid+1, right+1):
                if list[index] < list[i]:
                    temp += 1
                # if list[index] >= list[i]:
                #     break
            self.sum += temp * list[index]
            index += 1
        self.merge(list, left, mid, mid+1, right)
        
        return
        
def small_sum_2(list: list):
    if len(list) ==0 or list == None:
        return 0
    sum = 0
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] < list[j]:
                sum += list[i]

    return sum


test = [3,1 ,7,0, 2]

small_sum_obj = SamllSum()
result= small_sum_obj.small_sum(test)
# result = small_sum_2(test)
print(result)