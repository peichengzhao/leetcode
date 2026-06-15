from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def get_k_b(A: List[int], B: List[int]):
            num1, num2 = B[1]-A[1], B[0]-A[0]
            if num2 == 0:
                return [float("inf"), A[0]]
            k = num1 / num2
            b = A[1] - k*A[0]
            return [k, b]
        hash_map = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                temp = get_k_b(points[i], points[j])
                if tuple(temp) in hash_map:
                    if i not in hash_map[tuple(temp)]:
                        hash_map[tuple(temp)].add(i)
                    if j not in hash_map[tuple(temp)]:
                        hash_map[tuple(temp)].add(j)
                else:
                    hash_map[tuple(temp)] = set()
                    hash_map[tuple(temp)].add(i)
                    hash_map[tuple(temp)].add(j)
        result = 1
        for key, value in hash_map.items():
            result = max(result, len(value))
        return result



