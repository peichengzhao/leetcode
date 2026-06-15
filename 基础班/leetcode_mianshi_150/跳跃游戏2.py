from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0     # 初始化跳跃次数为 0
        end = 0       # 第一步的边界初始化为 0
        max_pos = 0   # 全局最远位置初始化为 0

        # 重点：遍历到 len(nums)-1 就停止！
        # 因为到最后一个位置不需要再跳了
        for i in range(len(nums)-1):
            # 1. 遍历每一个位置，更新【能跳到的最远位置】
            # 当前位置i能跳到 i + nums[i]，和max_pos比，保留大的
            max_pos = max(max_pos, nums[i] + i)

            # 2. 关键！如果遍历到了【当前步的边界】
            # 说明：这一步能跳的位置都走完了，必须跳下一步！
            if i == end:
                steps += 1          # 跳跃次数 +1
                end = max_pos      # 更新边界为新的最远位置

        # 遍历结束，返回总步数
        return steps






from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        step = 0
        n = len(nums)
        current = 0
        max_pos = 0
        current_end = 0
        for i in range(n):
            max_pos = max(max_pos, i+nums[i])
            if i == current_end:
                step += 1
                current_end = max_pos
                if current_end >= n-1:
                    break
        return step

        
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        step = 0
        length = len(nums)
        current = 0
        while current < length-1:
            max_reach = nums[current]
            if current + max_reach >= length -1:
                return step + 1
            far_pos = current
            best_next = current          
            for i in range(current+1, current + max_reach + 1):
                if i + nums[i] > far_pos:  # 找到能使下一步最远的落脚点
                    far_pos = i + nums[i]
                    best_next = i
            step += 1
            current = best_next           # 跳到那个中间位置
        return step