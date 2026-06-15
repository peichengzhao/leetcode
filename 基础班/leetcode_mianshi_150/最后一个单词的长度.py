from typing import List
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        help_list = s.split()
        return len(help_list[-1]) if help_list else 0