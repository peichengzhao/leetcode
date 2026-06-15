from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        step = (m + n) // 2
        if (m + n) % 2 == 0:
            #说明是双数
            temp1, temp2 = 0, 0
            res1, res2 = 0, 0
            while temp1 < m and temp2 < n:
                cur = min(nums1[temp1], nums2[temp2])
                if step == 1:
                    res1 = cur
                if step == 0:
                    res2 = cur
                if nums1[temp1] <= nums2[temp2]:
                    temp1 += 1
                elif nums1[temp1] > nums2[temp2]:
                    temp2 += 1
                step -= 1
            if temp1 < m:
                while step >= 0:
                    if step == 1:
                        res1 = nums1[temp1]
                    elif step == 0:
                        res2 = nums1[temp1]
                    temp1 += 1
                    step -= 1
            elif temp2 < n:
                while step >= 0:
                    if step == 1:
                        res1 = nums2[temp2]
                    elif step == 0:
                        res2 = nums2[temp2]
                    temp2 += 1
                    step -= 1 
            return (res1 + res2) / 2
        elif (n + m) % 2 != 0:
            temp1, temp2 = 0, 0
            while temp1 < m and temp2 < n:
                cur = min(nums1[temp1], nums2[temp2])
                if step == 0:
                    return cur
                if nums1[temp1] <= nums2[temp2]:
                    temp1 += 1
                elif nums1[temp1] > nums2[temp2]:
                    temp2 += 1
                step -= 1
            if temp1 < m:
                while True:
                    if step == 0:
                        return nums1[temp1]
                    temp1 += 1
                    step -= 1
            elif temp2 < n:
                while True:
                    if step == 0:
                        return nums2[temp2]
                    temp2 += 1
                    step -= 1 



#舒服一些的写法 

# 看到log  想到二分法
from typing import List

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