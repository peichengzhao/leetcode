# from typing import List

# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         if n == 0 or n == 2 or n == 3:
#             return []
#         if n == 1:
#             return [["Q"]]
#         record = [0] * n
#         results = []
#         self.process(0, record, n, results)
#         results = self.change_to_path(results)
#         return results

#     def process(self, row: int, record: List[List[str]], n: int, results: List[List[str]]):
#         if row == n:
#             results.append(record.copy())
#             return
#         for col in range(n):
#             if self.check_valid(row, col, record):
#                 record[row] = col
#                 self.process(row+1, record, n, results)
#             else:
#                 continue
#         return
#     def check_valid(self, row: int, col: int, record: List[List[str]]):
#         for i in range(row):
#             if record[i] == col or abs(row - i) == abs(col - record[i]):
#                 return False
#         return True
#     def change_to_path(self, records: List[List[int]]) -> List[List[str]]:
#         results = []
#         for record in records:  # 遍历每个解（每行皇后的列索引）
#             board = []
#             for col in record:  # 遍历每行皇后的列索引
#                 # 正确生成每行的字符串：col列是Q，其余是.
#                 row_str = "." * col + "Q" + "." * (len(record) - col - 1)
#                 board.append(row_str)
#             results.append(board)
#         return results





from typing import List
 #优化版本
 
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0 or n == 2 or n == 3:
            return []
        if n == 1:
            return [["Q"]]
        record = [0] * n
        results = []
        limit = (1 << (n+1)) -1
        lie_limit = 0
        left_limit = 0
        right_limit = 0

        return results

    def process(self, lie_limit: int, left_limit: int, right_limit: int, results: List[List[str]] ,record: List[int], limit: int):
        if lie_limit == limit:
            results.append(record.copy()) # 如果lie_limit == limit，说明已经放置了所有的皇后，将record复制到results中
            return 
        pos = limit & (~(lie_limit | left_limit | right_limit))
        most_right_one = 0
        res = 0
        while pos != 0:
            most_right_one = pos & (~pos + 1)
            
            


    def check_valid(self, row: int, col: int, record: List[List[str]]):
        for i in range(row):
            if record[i] == col or abs(row - i) == abs(col - record[i]):
                return False
        return True

    def change_to_path(self, records: List[List[int]]) -> List[List[str]]:
        results = []
        for record in records:  # 遍历每个解（每行皇后的列索引）
            board = []
            for col in record:  # 遍历每行皇后的列索引
                # 正确生成每行的字符串：col列是Q，其余是.
                row_str = "." * col + "Q" + "." * (len(record) - col - 1)
                board.append(row_str)
            results.append(board)
        return results






# N皇后问题

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0 or n == 2 or n == 3:
            return None
        if n == 1:
            return [["Q"]]
        row, col = 0, 0
        results = []
    
    def check_vaild()
        



###只要新皇后的 行 + 列、行−列，和之前任何一个皇后重复，就说明在同一条斜线上，不能放！
#列冲突：i in 已用列
# 左斜线冲突（↙）：行号 - 列号 相同
# 右斜线冲突（↘）：行号 + 列号 相同


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 2 or n == 3:
            return []
        result = []
        path = []
        hangshu = 0
        def process(hangshu: int, path: List[str], left_limit: List[int], right_limit: List[int], Q_limit: List[int]):
            if hangshu == n:
                result.append(path.copy())
                return 
            for i in range(n):
                if i in Q_limit or hangshu + i in left_limit or hangshu - i in right_limit:
                    continue
                temp = "." * i + "Q" + "." *(n-1-i)
                path.append(temp)
                # 得到限制
                Q_limit.append(i)
                left_limit.append(hangshu+i)
                right_limit.append(hangshu-i)
                process(hangshu+1, path, left_limit, right_limit, Q_limit)
                left_limit.pop()
                right_limit.pop()
                Q_limit.pop()
                path.pop()
        process(0, [], [], [], [])
        return result




