from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #构造temp_list
        if numRows == 1 or numRows >= len(s):
            return s
        temp_list = []
        for i in range(numRows):
            temp_list.append(i)
        for j in range(numRows-2, 0, -1):
            temp_list.append(j)
        count = 0
        temp = 0
        length = 2 * numRows - 2
        res = [""] * numRows
        for c in s:
            res[temp] += c
            count = (count+1) % length
            temp = temp_list[count]
        result = ""
        for k in res:
            result += k
        return result