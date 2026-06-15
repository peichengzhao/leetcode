from typing import List, Optional

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # log 复杂度 考虑二分
        left, right = 0, len(nums)-1
        middle = (left + right) // 2
        def process(nums: List[int], left: int, right: int, target: int):
            while left <= right:
                middle = (left + right) // 2 
                if nums[middle] == target:
                    return middle
                elif nums[middle] > target:
                    right = middle-1
                else:
                    left = middle + 1
            return -1

        while left <= right:
            middle = (left + right) // 2 
            if nums[middle] == target:
                return middle
            if nums[middle] > nums[right]:
                # middle 在左边
                if target <= nums[right]:
                    left = middle + 1
                else:
                    if nums[middle] > target:
                        return process(nums, left, middle-1, target)
                    else:
                        left = middle + 1
            else:
                if target > nums[right]:
                    right = middle - 1
                else:
                    if nums[middle] < target:
                        return process(nums, middle+1, right, target)
                    else:
                        right = middle - 1
        return -1



#上面的写法 感觉有点笨蛋
