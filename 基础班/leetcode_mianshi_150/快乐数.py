class Solution:
    def isHappy(self, n: int) -> bool:
        hash_map = set()
        if n == 1:
            return True
        def process(number: int):
            result = 0
            while number > 0:
                temp = number % 10
                result += temp ** 2
                number = number // 10
            return result
        hash_map.add(n)
        while n != 1:
            n = process(n)
            if n in hash_map:
                return False
            else:
                hash_map.add(n)
    
        return True

