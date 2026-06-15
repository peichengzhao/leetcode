from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                continue
            left_num, right_num = num-1, num+1
            if left_num not in hash_map and right_num not in hash_map:
                hash_map[num] = [1, num, num]
            elif left_num in hash_map and right_num not in hash_map:
                left_length = hash_map[left_num][0]
                left_num_left = hash_map[left_num][1]
                left_num_right = hash_map[left_num][2]
                hash_map[num] = [left_length+1, left_num_left, num]
                hash_map[left_num_left] = [left_length+1, left_num_left, num]
            elif left_num not in hash_map and right_num in hash_map:
                right_length = hash_map[right_num][0]
                right_num_left = hash_map[right_num][1]
                right_num_right = hash_map[right_num][2]
                hash_map[num] = [right_length+1, num, right_num_right]
                hash_map[right_num_right] = [right_length+1, num, right_num_right]
            else:
                left_length = hash_map[left_num][0]
                right_length = hash_map[right_num][0]
                left_num_left = hash_map[left_num][1]
                right_num_right = hash_map[right_num][2]
                hash_map[num] = [left_length+right_length+1, left_num_left, right_num_right]
                hash_map[left_num_left] = [left_length+right_length+1, left_num_left, right_num_right]
                hash_map[right_num_right] =[left_length+right_length+1, left_num_left, right_num_right]
        max_length = 0
        for key, value in hash_map.items():
            max_length = max(max_length, value[0])
        return max_length
