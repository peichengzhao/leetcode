from typing import List



class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = True
        length = len(digits)
        i = length - 1
        while i >=0 and temp:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                temp = False
                break
            i -= 1
        if temp:
            digits.append(0)
            for i in range(1, len(digits)):
                digits[i] = digits[i-1]
            digits[0] = 1
        return digits


            
