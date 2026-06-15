from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        n = len(s)#字符串长度
        def process(index: int):
            if index == n:
                result.append(path.copy())
                return 
            for i in range(index, n):
                new_str = s[index:i+1]
                if new_str == new_str[::-1]:
                    # 说明有效
                    path.append(new_str)
                    process(i+1)
                    path.pop()
        process(0)
        return result
        