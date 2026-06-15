from typing import List

#超时

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * len(ratings)
        is_continue = True
        while is_continue:
            is_continue = False
            for i in range(len(candy)):
                #不满足
                if (i>0 and candy[i-1] >= candy[i] and ratings[i-1] < ratings[i]) or (i<n-1 and candy[i+1] >= candy[i] and ratings[i+1] < ratings[i]):
                    is_continue = True
                    candy[i] += 1
        res = 0 
        for i in range(len(candy)):
            res += candy[i]
        return res


# AC解 两边扫描一次找出左边大于右边的 一次找出右边大于左边的
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = 0
        candy = [1] * len(ratings)
        for i in range(len(ratings)):
            if i > 0 and ratings[i] > ratings[i-1]:
                candy[i] = max(candy[i-1] + 1, candy[i])
        for j in range(len(ratings)-1, -1,-1):
            if j < len(ratings) - 1 and ratings[j] > ratings[j+1]:
                candy[j] = max(candy[j+1] + 1, candy[j]) 
        for k in range(len(candy)):
            res += candy[k]
        return res