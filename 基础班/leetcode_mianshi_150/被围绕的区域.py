from typing import List
# 超时解
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board) ,len(board[0])
        def dfs(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            elif board[i][j] == "X":
                return 
            elif board[i][j] == "O":
                board[i][j] = "#"
                dfs(i-1, j)
                dfs(i+1, j) 
                dfs(i, j-1)
                dfs(i, j+1)
            return 
        #看边缘  
        for i in range(m):
            if board[i][0] == "O":
                #up
                dfs(i, 0)
            if board[i][n-1] == "O":
                dfs(i, n-1)
        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m-1][j] == "O":
                dfs(m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"




