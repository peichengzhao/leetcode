from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        relation = {"2":["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        result = []
        length = len(digits)
        def process(index: int, temp: str):
            nonlocal length, result, digits
            if index == length:
                result.append(temp)
                return 
            else:
                cur = digits[index]
                candidates = relation[cur]
                for candidate in candidates:
                    temp += candidate
                    process(index+1, temp)
                    temp = temp[:-1]
        process(0, "")
        return result