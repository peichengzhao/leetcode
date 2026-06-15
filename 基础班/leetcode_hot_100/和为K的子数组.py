from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        
        hash_map = {0: 1}  # 初始前缀和0出现1次
        results = 0
        cur_sum = 0
        
        # 修正1：遍历所有元素（从索引0开始）
        for num in nums:  # 或 for i in range(len(nums))，用num = nums[i]更直观
            cur_sum += num  # 累加当前元素，更新前缀和
            
            # 修正2：先统计符合条件的结果，再更新哈希表
            if (cur_sum - k) in hash_map:
                results += hash_map[cur_sum - k]
            
            # 优化：用get简化哈希表更新
            hash_map[cur_sum] = hash_map.get(cur_sum, 0) + 1
        
        return results







from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        result = 0
        pre_sum = 0
        hash_map = {}
        for i in range(len(nums)):
            pre_sum += nums[i]
            temp = k - pre_sum
            if temp in hash_map:
                result += hash_map[temp]
            if pre_sum not in hash_map:
                hash_map[pre_sum] = 1
            if pre_sum in hash_map:
                hash_map[pre_sum] += 1
        return result
            

        
























