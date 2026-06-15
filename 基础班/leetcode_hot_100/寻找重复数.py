from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def change(nums: List[int], i: int, j: int):
            nums[i], nums[j] = nums[j], nums[i]
            return 
        # nums.length == n + 1
        while True:
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue
                if nums[nums[i]] == 0:
                    return nums[i]
                temp = nums[i]
                change(nums, i, nums[i])
                nums[temp] = 0





#利用快慢指针的说法 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        length = len(nums)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow




