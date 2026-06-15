from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        left, right = 0, length
        def process()
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                temp_left = left
                temp_sum = sum
                while temp_sum <= target:
                    if temp_sum == target:
                        return [temp_left+1, right+1]
                    elif temp_sum < target:
                        temp_left += 1
                        temp_sum += numbers[temp_left]
                        continue
                    else:
                        break
                right -= 1
            else:
                temp_right = right
                temp_sum = sum
                while temp_sum >= target:
                    if temp_sum == target:
                        return [left+1, temp_right+1]
                    elif temp_sum > target:
                        temp_right -= 1
                        temp_sum -= numbers[temp_right]
                        continue
                    else:
                        break
                left -= 1
            





from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left+1, right+1]
























