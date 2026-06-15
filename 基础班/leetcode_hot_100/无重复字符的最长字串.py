class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == None or len(s) == 0:
            return 0
        max_length = 1
        left, right = 0, 1
        hash_map = {}
        hash_map[s[0]] = True
        while right < len(s):
            if s[right] not in hash_map:
                max_length = max(max_length, right- left + 1)
                hash_map[s[right]] = True
                right += 1
            else:
                hash_map.pop(s[left])
                left += 1
        return max_length







class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        hash_map = {}
        max_length = 0
        for i in range(len(s)):
            temp = ""
            hash_map = {}
            temp_length = 0
            for j in range(i+1, len(s)):
                if s[j] not in hash_map:
                    hash_map[s[j]] = True
                    temp_length += 1
                    temp.join(str(s[j]))
                    if temp_length > max_length:
                        result = temp
                        max_length = temp_length
                else:
                    break
        return len(result)


# 滑动窗口写法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        hash_map = {}
        max_length = 1
        left, right = 0, 1
        hash_map[s[0]] = True
        temp_length = 1
        while right < len(s):
            if s[right] not in hash_map:
                hash_map[s[right]] = True
                temp_length += 1
                right += 1
                if temp_length > max_length:
                    max_length = temp_length
            else:
                temp_length -= 1
                hash_map.pop(s[left])
                left += 1
        return max_length


