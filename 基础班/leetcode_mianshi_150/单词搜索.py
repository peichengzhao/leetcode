from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length = len(word)
        if length == 0:
            return True
        row, col = len(board), len(board[0])
        def process(index: int, i: int, j: int):
            if index == length:
                return True
            if i<0 or i>=row or j<0 or j>=col or word[index] != board[i][j]:
                return False
            temp = board[i][j] 
            board[i][j] = "#"
            res = process(index+1, i-1, j) or process(index+1, i+1, j) or process(index+1, i, j-1) or process(index+1, i, j+1)
            board[i][j] = temp
            return res
        for i in range(row):
            for j in range(col):
                res = process(0, i, j)
                if res == True:
                    return True
        return False
                