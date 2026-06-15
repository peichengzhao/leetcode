from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                is_ok = self.search(board, word, 0, i, j)
                if is_ok:
                    return True
        return False

    def search(self, board: List[List[str]], word: str, index: int, i: int, j: int):
        if index == len(word):
            return True
        if i<0 or i>= len(board) or j<0 or j>=len(board[0]):
            return False
        if board[i][j] != word[index]:
            return False
        if board[i][j] == word[index]:
            temp = board[i][j]
            board[i][j] = "#"
            # 向上
            up = self.search(board, word, index+1,i-1, j)
            # 向下
            down = self.search(board, word, index+1,i+1, j)
            # 向左
            left = self.search(board, word, index+1,i, j-1)
            # 向右
            right = self.search(board, word, index+1,i, j+1)
            board[i][j] = temp
            return up or down or left or right
