def xuanze(list:list):
    if len(list) == 0 or len(list) == 1:
        return list
    for i in range(0, len(list)):
        j = i
        while j > 0 and list[j-1] > list[i]:
            swap(list, j, j-1)
            j -= 1
    return list
test = [2,3, 1, 5, 4]
print(xuanze(test))


class Solution:
    def __init__(self):
        pass
    def xuanze(list:list):
        if len(list) == 0 or len(list) == 1:
            return list
        for i in range(0, len(list)):
            j = i
            while j > 0 and list[j-1] > list[i]:
                swap(list, j, j-1)
                j -= 1
        return list

test = [2,3, 1, 5, 4]
solver = Solution()
print(solver.xuanze(test))