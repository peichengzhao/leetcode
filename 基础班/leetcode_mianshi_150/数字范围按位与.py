class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 不断把 right 最右边的1消成0，直到 left >= right
        while left < right:
            right &= right - 1
        return right