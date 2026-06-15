from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        stack = []
        answer = [0] * len(temperatures)
        stack.append(0)
        pop_value = 0 
        for i in range(1, len(temperatures)):
            while stack and temperatures[pop_value] < temperatures[i]:
                pop_value = stack.pop()
                answer[pop_value] = i - pop_value
                if stack:
                    pop_value = stack[-1]
            stack.append(i)
            pop_value = stack[-1]
        return answer

