from typing import List

#超出时间限制
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k:
            self.youyi(nums)
            k -= 1
        return 
    
    def youyi(self, nums: List[int]):
        temp = nums[-1]
        for i in range(len(nums)-1, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = temp
        return
        


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        help_list = []
        k = k % len(nums)
        for i in range(1, k+1):
            help_list.append(nums[-i])
        help_list.reverse()
        for j in range(len(nums)-1-k, -1, -1):
            nums[j+k] = nums[j]
        for i in range(k):
            nums[i] = help_list[i]
        return 






class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse_function(nums, 0, len(nums)-1)
        self.reverse_function(nums, 0, k-1)
        self.reverse_function(nums, k, len(nums)-1)
        return 
    

    def reverse_function(arr: List[int], begin: int, end: int):
        if begin >= end:
            return
        while end > begin:
            arr[begin], arr[end] = arr[end], arr[begin]
            begin += 1
            end -= 1
        return 

        