from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_limit = [set() for _ in range(9)]
        col_limit = [set() for _ in range(9)]
        sub_box_has = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == "":
                    continue
                box_idx = (i//3) * 3 + (j//3)
                if num in row_limit[i] or num in col_limit[j] or num in sub_box_has[box_idx]:
                    return False
                row_limit[i].add(num)
                col_limit[j].add(num)
                sub_box_has[box_idx].add(num)
        return True

        