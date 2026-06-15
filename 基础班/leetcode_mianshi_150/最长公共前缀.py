from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 边界1：空数组直接返回空
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        min_length = len(strs[0])
        
        # 遍历相邻字符串，计算两两公共前缀
        for i in range(len(strs)-1):
            s1 = strs[i]
            s2 = strs[i+1]
            temp = 0
            # 对比字符，统计公共前缀长度
            while temp < len(s1) and temp < len(s2):
                if s1[temp] == s2[temp]:
                    temp += 1
                else:
                    break
            # 取最小的公共前缀（始终是整数）
            min_length = min(min_length, temp)
        
        # ✅ 修复2：用整数切片，无报错
        return strs[0][:min_length]




class Solution:
    def reverseWords(self, s: str) -> str:
        help_list = s.split()
        help_list = reversed(help_list)
        result = ""
        for s in help_list:
            result += s
            result += " "
        return result[:-1]







class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        