from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 肯定使用二分 但是怎么分呢
        def find_first(left: int, right: int):
            while left <= right:
                middle = (left+right) // 2
                if nums[middle] == target:
                    result = middle
                    temp = find_first(left, middle-1)
                    while temp != -1:
                        result = temp
                        temp = find_first(left, result-1)
                    return result
                elif nums[middle] > target:
                    right = middle -1
                else:
                    left = middle + 1
            return -1
        def find_last(left:int, right: int):
            while left <= right:
                middle = (left+right) // 2
                if nums[middle] == target:
                    result = middle
                    temp = find_last(result+1, right)
                    while temp != -1:
                        result = temp
                        temp = find_last(result+1, right)
                    return result
                elif nums[middle] > target:
                    right = middle -1
                else:
                    left = middle + 1
            return -1
        left, right = find_first(0, len(nums)-1), find_last(0, len(nums)-1)
        return [left, right]