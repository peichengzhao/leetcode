from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        chars = ["A", "C", "G", "T"]
        queue = deque([(startGene, 0)])
        set_list = set(bank)
        while queue:
            # 八个字母的替换
            temp_str, temp_step = queue.popleft()
            for i in range(len(temp_str)):
                for Q in chars:
                    if Q == temp_str[i]:
                        continue
                    new_str = temp_str[:i] + Q + temp_str[i+1:]
                    if new_str == endGene:
                        return temp_step + 1
                    elif new_str not in set_list:
                        continue
                    else:
                        set_list.remove(new_str)
                        queue.append([new_str, temp_step + 1])
        return -1