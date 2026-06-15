from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        size = len(heights)
        stack.append(0)
        max_result = float("-inf")
        for i in range(size):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                while len(stack) > 0 and cur_height == heights[stack[-1]]:
                    stack.pop()
                if len(stack) > 0:
                    cur_width = i - stack[-1] - 1
                else :
                    cur_width = i
                max_result = max(max_result, cur_width * cur_height)
            stack.append(i)
        while len(stack) > 0:
            cur_height = heights[stack.pop()]
            while len(stack) > 0 and cur_height == heights[stack[-1]]:
                stack.pop() # 去重
            if len(stack) > 0:
                cur_width = size - stack[-1] - 1
            else:
                cur_width = size
            max_result = max(max_result, cur_height * cur_width)

        return max_result

