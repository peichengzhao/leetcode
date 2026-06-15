from functools import cache
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or target <= 0:
            return []
        results = []
        path = []
        self.process(candidates, 0, target, path, results)
        return results
    def process(self, candidates: List[int], index: int, rest: int, path: List[int], results: List[List[int]]):
        if rest < 0:
            return
        if rest == 0:
            results.append(path.copy())
            return 
        if index == len(candidates):
            return 
        candidate = candidates[index]
        count = rest // candidate
        if count == 0:
            self.process(candidates, index + 1, rest, path, results)
            return 
        for i in range(0, count + 1):
            new_path = path.copy()
            new_path.extend([candidate] * i)
            self.process(candidates, index + 1, rest - candidate * i, new_path, results)
        return 
        







class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates :
            return []
        result = []
        
    def process(self, candidates: List[int], target: int,cur_number: int, cur_sum: int, path: List[int], result: List[int]):
        if cur_sum > target:
            return
        elif cur_sum == target:
            result.append(path)
            return 
        else:
            rest = target - cur_sum
            count = rest // candidates[cur_number]
            if count == 0:
                self.process(self, candidates, target, cur_number+1, cur_sum, path, result)
            for i in range(count):
                self.process(self, candidates, target, cur_number, cur_sum+candidates[cur_number]*count, path.append(candidates[cur_number]), result)
                












class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        @cache
        def dfs(i: int) -> int:
            if i == 0:  # 爬完了
                return 1
            return sum(dfs(i - x) for x in nums if x <= i)  # 枚举所有可以爬的台阶数
        return dfs(target)


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        @cache
        def dfs(i: int) -> int:
            if i == 0:
                return 1
            return sum(dfs(i - x) for x in nums if x <= i)
        return dfs(target)

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            temp = 0
            for num in nums:
                if i >= num:
                    dp[i] += dp[temp-num]
        return dp[-1]















