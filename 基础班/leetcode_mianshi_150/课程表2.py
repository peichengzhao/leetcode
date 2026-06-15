from typing import List

from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        in_degree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            in_degree[a] += 1
            graph[b].append(a)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0
        while queue:
            temp = queue.popleft()
            result.append(temp)
            count += 1
            for course in graph[temp]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)
        return result if count == numCourses else []