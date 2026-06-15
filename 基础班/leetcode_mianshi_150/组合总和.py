from typing import List
from unittest import result

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        used = set()
        result = []
        temp = []
        def process(temp_sum: int):
            if temp_sum == target:
                sorted_temp = tuple(sorted(temp))
                if sorted_temp in used:
                    return
                else:
                    result.append(temp.copy())
                    used.add(sorted_temp)
            elif temp_sum > target:
                return 
            else:
                for candidate in candidates:
                    temp_sum += candidate
                    temp.append(candidate)
                    process(temp_sum)
                    temp_sum -= candidate
                    temp.pop()
        process(0)
        return result




class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        used = set()
        index = 0
        temp_sum = 0
        result = []
        temp = []
        length = len(candidates)
        def process(index: int):
            nonlocal temp_sum
            if temp_sum == target:
                result.append(temp.copy())
                return 
            elif temp_sum > target:
                return 
            else:
                for i in range(index, length):
                    temp_sum += candidates[i]
                    temp.append(candidates[i])
                    process(i)
                    temp_sum -= candidates[i]
                    temp.pop()
        process(0)
        return result



