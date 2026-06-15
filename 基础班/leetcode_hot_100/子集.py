from tracemalloc import start
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        results = []
        temp = []
        self.process(nums, 0, temp, results)
        return results
    
    def process(self, nums: List[int], start: int, temp: List[int], results: List[List[int]]):
        results.append(temp.copy())
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.process(nums, i+1, temp, results)
            temp.pop()
        return 





class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []
        start = 0
        self.process(nums, start, temp, result)
        return result


    def process(self, nums: List[int], start: int, temp: List[int], result: List[List[int]]):
        result.append(temp.copy())
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.process(nums, i+1, temp, result)
            temp.pop()
        return 


