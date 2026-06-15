from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_s = ""
        for i in range(len(s)):
            if s[i] >= "a" and s[i] <= "z":
                clear_s += s[i]
            elif s[i] >= "A" and s[i] <= "Z":
                clear_s += chr(ord(s[i]) - ord("A") + ord("a"))
            elif s[i] >= "0" and s[i] <= "9":
                clear_s += s[i]
        left, right = 0, len(clear_s)-1
        while left <= right:
            if clear_s[left] != clear_s[right]:
                return False
            else:
                left += 1 
                right -= 1
        return True



#使用isalnum() 函数 .lower() 来转小写


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_s = [c.lower() for c in s if c.isalnum()]
        return clear_s == clear_s[::-1]