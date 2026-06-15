from typing import List
# 笨蛋方法
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        def change(str_1: str):
            temp = []
            for c in str_1:
                temp.append(ord(c))
            temp = sorted(temp)
            result = ""
            for number in temp:
                result += chr(number)
            return result
        hash_map = {}
        for stc in strs:
            sorted_str = change(stc)
            if sorted_str not in hash_map:
                hash_map[sorted_str] = [stc]
            else:
                hash_map[sorted_str].append(stc)
        result = []
        for key, value in hash_map.items:
            result.append(value)
        return result



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for stc in strs:
            sorted_str = sorted(stc)
            if sorted_str not in hash_map:
                hash_map[sorted_str] = [stc]
            else:
                hash_map[sorted_str].append(stc)
        result = []
        for key, value in hash_map.items():
            result.append(value)
        return result

