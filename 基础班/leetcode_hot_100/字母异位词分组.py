from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0 :
            return [[]]
        hash_map = {str: []}
        for i in range(len(strs)):
            sorted_str = self.sort_str(strs[i])
            if sorted_str not in hash_map:
                hash_map[sorted_str] = [strs[i]]
            else:
                hash_map[sorted_str].append(strs[i])
        result = []
        for key in hash_map:
            temp_list = hash_map[key]
            result.append(temp_list)
        return result

    def sort_str(self, input_str: str) -> str:
        if len(input_str) == 0:
            return ""
        temp_str = []
        for i in range(len(input_str)):
            temp_str.append(input_str[i])
        temp_str = sorted(temp_str)
        result_str = "".join(temp_str)
        return result_str














class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        hash_map_str = {}
        number = 0
        results = []
        for str_1 in strs:
            sorted_str = self.sort_str(str_1)
            if sorted_str not in hash_map_str:
                hash_map_str[sorted_str] = [str_1]
            else:
                hash_map_str[sorted_str].append(str_1)
        for key in hash_map_str:
            results.append(hash_map_str[key])
        return results

    
    def sort_str(self, input_str: str):
        if len(input_str) == 0:
            return ""
        temp_str = []
        for i in range(len(input_str)):
            temp_str.append(input_str[i])
        temp_str = sorted(temp_str)
        result_str = "".join(temp_str)
        return result_str