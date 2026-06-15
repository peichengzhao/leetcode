from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        hash_map = set()
        length = len(nums)
        temp = []
        def process(index: int):
            if index == length:
                result.append(temp.copy())
                return 
            else:
                for num in nums:
                    if num in hash_map:
                        continue
                    else:
                        temp.append(num)
                        hash_map.add(num)
                        process(index+1)
                        temp.pop()
                        hash_map.remove(num)
        process(0)
        return result

