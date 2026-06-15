from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        hash_set = {}
        results = []
        temp = []
        self.process(nums, temp, hash_set, results)
        return results

    
    def process(self, nums: List[int], temp: List[int], hash_set: dict, results: List[List[int]]):
        if len(temp) == len(nums):
            results.append(temp.copy())
            return
        for i in range(len(nums)):
            if nums[i] not in hash_set:
                hash_set[nums[i]] = 1
                temp.append(nums[i])
                self.process(nums, temp, hash_set, results)
                temp.pop()
                hash_set.pop(nums[i])
            else:
                continue
        return 
