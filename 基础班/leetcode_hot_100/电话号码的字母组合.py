from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {'2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']}
        path = ""
        results = []
        index = 0
        self.process(digits, index, path, results, phone)
        return results


    def process(self, digits: str, index: int, path: str, results: List[str], phone: dict):
        if index == len(digits):
            results.append(path)
            return
        temp = digits[index]
        help_list = phone[temp]
        for help in help_list:
            path += help
            self.process(digits, index+1, path, results, phone)
            path = path[:-1]
        return 
