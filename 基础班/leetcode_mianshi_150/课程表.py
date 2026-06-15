from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash_map = {}
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            in_degree[a] += 1
            if b not in hash_map:
                hash_map[b] = [a]
            else:
                hash_map[b].append(a)
        is_continue = True
        count = 0
        while is_continue and count != numCourses:
            is_continue = False
            for i in range(len(in_degree)):
                if in_degree[i] == 0:
                    is_continue = True
                    count += 1
                    if i in hash_map:
                        need = hash_map[i]
                        for num in need:
                            in_degree[num] -= 1
                else:
                    continue
        return count == numCourses


from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = [[]for _ in range(numCourses)]
        for a, b in prerequisites:
            in_degree[a] += 1
            graph[b].append(a)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0
        while queue:
            course = queue.popleft()
            count += 1
            for i in graph[course]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
        return count == numCourses