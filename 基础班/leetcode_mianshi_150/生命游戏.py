from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                number = 0
                if i-1 >=0 and (board[i-1][j]==1 or board[i-1][j]==3):
                    number += 1
                if i-1 >=0 and j-1 >=0 and (board[i-1][j-1]==1 or board[i-1][j-1]==3):
                    number += 1
                if i-1 >=0 and j+1 <=n-1 and (board[i-1][j+1]==1 or board[i-1][j+1]==3):
                    number += 1
                if j-1 >= 0 and (board[i][j-1]==1 or board[i][j-1]==3):
                    number += 1
                if j+1 < n and (board[i][j+1]==1 or board[i][j+1]==3):
                    number += 1
                if i+1 <m and (board[i+1][j]==1 or board[i+1][j]==3):
                    number += 1
                if i+1 < m and j-1 >=0 and (board[i+1][j-1]==1 or board[i+1][j-1]==3):
                    number += 1
                if i+1 < m and j+1 < n and (board[i+1][j+1]==1 or board[i+1][j+1]==3):
                    number += 1
                if number < 2:
                    board[i][j] = 3 if board[i][j] == 1 else 0
                elif number == 2:
                    board[i][j] = board[i][j]
                elif number == 3 and board[i][j] == 0:
                    board[i][j] = 4
                elif number ==3 and board[i][j] == 1:
                    board[i][j] = 1
                else:
                    board[i][j] = 3 if board[i][j] == 1 else 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 4:
                    board[i][j] = 1
                else:
                    continue
        return 