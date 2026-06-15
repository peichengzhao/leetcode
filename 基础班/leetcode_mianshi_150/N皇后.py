from typing import List

class Solution:
    def totalNQueens(self, n: int) -> int:
        if n==1:
            return 1
        if n <= 3:
            return 0
        pos_limit = set()
        diag1 = set()
        diag2 = set()
        result = 0
        def process(index: int):
            if index == n:
                result += 1
                return
            for i in range(n):
                if i not in pos_limit and (index - i) not in diag1 and (index+i) not in diag2:
                    pos_limit.append(i)
                    diag1.append(index-i)
                    diag2.append(index+i)
                    process(index+1)
                    pos_limit.remove(i)
                    diag1.remove(index-i)
                    diag2.remove(index+i)
        process(0)
        return result



class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n==1:
            return [["Q"]]
        if n <= 3:
            return []
        pos_limit = set()
        diag1 = set()
        diag2 = set()
        result = []
        path = []
        def process(index: int, path: List[str]):
            if index == n:
                result.append(path)
                return
            for i in range(n):
                if i not in pos_limit and (index - i) not in diag1 and (index+i) not in diag2:
                    pos_limit.append(i)
                    diag1.add(index-i)
                    diag2.add(index+i)
                    temp = "." * i + "Q" + "."(n-i-1)
                    path.add(temp)
                    process(index+1)
                    pos_limit.remove(i)
                    diag1.remove(index-i)
                    diag2.remove(index+i)
                    path.pop()
        process(0, path)
        return result