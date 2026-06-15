class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            mid_sq = mid * mid
            if mid_sq == x:
                return mid
            elif mid_sq < x:
                l = mid + 1
            else:
                r = mid - 1
        return r