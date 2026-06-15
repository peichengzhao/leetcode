from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        left1, left2, right1, right2 = 0, 0, m-1, n-1
        count_m, count_n = m, n
        middle = (m+n) // 2
        res = [0] * ((m+n) // 2 + 1)
        step = 0
        res_count = 0
        final_count = (m+n) // 2 + 1
        while step <= (m+n) // 2 + 1:
            count = ((count_m + count_n) // 2 + 1 - res_count)
            value_number1 = nums1[left1+count]
            value_number2 = nums2[left2+count]
            if value_number1 < value_number2:
                res_count += count
                res[step: step+count] = nums1[left1:left1+count]
                left1 = left1+count
                count_m -= count
                step += count
            else:
                res_count += count
                res[step: step+count] = nums1[left2: left2+count]
                left2 += count
                count_m -= count
                step += count
        return res[-2] if (m+n) // 2 ==1 else (res[-1] + res[-2]) // 2











class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 核心：找两个有序数组中第 k 小的元素
        def find_kth(n1: List[int], n2: List[int], k: int) -> int:
            # 边界：一个数组为空，直接返回另一个的第k个
            if not n1: return n2[k-1]
            if not n2: return n1[k-1]
            # 边界：找第1小，直接取最小值
            if k == 1: return min(n1[0], n2[0])
            
            # 二分：每次取 k//2 位置的元素，小的一侧全部排除
            i = min(len(n1), k//2)
            j = min(len(n2), k//2)
            if n1[i-1] < n2[j-1]:
                return find_kth(n1[i:], n2, k-i)
            else:
                return find_kth(n1, n2[j:], k-j)

        total = len(nums1) + len(nums2)
        # 奇数：找中间1个；偶数：找中间2个取平均
        if total % 2 == 1:
            return find_kth(nums1, nums2, total//2 + 1)
        else:
            left = find_kth(nums1, nums2, total//2)
            right = find_kth(nums1, nums2, total//2 + 1)
            return (left + right) / 2




class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def process(n1: List[int], n2: List[int], k: int):
            if not n1: return n2[k-1]
            if not n2: return n1[k-1]
            if k == 1:
                return min(n1[0], n2[0])
            temp1 = min(len(n1), k//2)
            temp2 = min(len(n2), k//2)
            if n1[temp1-1] < n2[temp2-1]:
                return process(n1[temp1:], n2, k-temp1)
            else:
                return process(n1, n2[temp2:], k-temp2)
        total_num = len(nums1) + len(nums2)
        if total_num % 2 == 1:
            return process(nums1, nums2, total_num//2+1)
        else:
            left = process(nums1, nums2, total_num//2)
            right = process(nums1, nums2, total_num//2+1)
            return (left+right) / 2







class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def process(n1: List[int], n2: List[int], k: int):
            #从两个有序数组中 拿到第K个元素
            if not n1: return n2[k-1]
            if not n2: return n1[k-1]
            if k == 1: return min(n1[0], n2[0])
            i = min(len(n1), k // 2)
            j = min(len(n2), k // 2)
            if n1[i-1] < n2[j-1]:
                return process(n1[i:], n2, k-i)
            else:
                return process(n1, n2[j:], k-j)
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return process(nums1, nums2, total//2+1)
        else:
            left = process(nums1, nums2, total//2)
            right = process(nums1, nums2, total//2+1)
            return (left+right) / 2















