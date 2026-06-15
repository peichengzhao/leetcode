from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                left_length = hash_map.get(nums[i] - 1, 0)
                right_legth = hash_map.get(nums[i] + 1, 0)
                hash_map[nums[i]] = left_length + right_legth + 1
                #更新边界
                hash_map[nums[i] - left_length + 1] = left_length + right_legth + 1
                hash_map[nums[i] + right_legth - 1] = left_length + right_legth + 1
        return max(hash_map.values())







class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        hash_map = {}
        max_length = 0
        for num in nums:
            if num not in hash_map:
                if num - 1 not in hash_map and num + 1 not in hash_map:
                    hash_map[num] = 1
                elif num - 1 not in hash_map and num + 1 in hash_map:
                    hash_map[num] = hash_map[num + 1] + 1
                    hash_map[hash_map[num] + num - 1] = hash_map[num]
                elif num - 1 in hash_map and num + 1 not in hash_map:
                    hash_map[num] = hash_map[num - 1] + 1
                    hash_map[num - hash_map[num] + 1] = hash_map[num]
                else:
                    hash_map[num] = hash_map[num + 1] + hash_map[num - 1] + 1
                    hash_map[num - hash_map[num - 1]] = hash_map[num]
                    hash_map[num + hash_map[num + 1]] = hash_map[num]
        for key in hash_map:
            if hash_map[key] > max_length:
                max_length = hash_map[key]
        return max_length
