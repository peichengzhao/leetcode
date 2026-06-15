import heapq

class MedianFinder:

    def __init__(self):

        self.small_part = []
        self.small_length = 0 
        self.big_part = []
        self.big_length = 0

    def addNum(self, num: int) -> None:
        if self.small_length > 0 and num <= self.small_part[0]:
            heapq.heappush(self.small_part, -num)
            self.small_length += 1
            if self.small_length > self.big_length + 1:
                self.small_length -= 1
                self.big_length += 1
                temp = -heapq.heappop(self.small_part)
                heapq.heappush(self.big_part, temp)
                return 
        elif self.big_length > 0 and num > self.big_part[0]:
            heapq.heappush(self.big_part, num)
            self.big_length += 1
            if self.big_length > self.small_length + 1:
                self.big_length -= 1
                self.small_length += 1
                temp = -heapq.heappop(self.big_part)
                heapq.heappush(self.small_part, temp)
                return  
        else:
            heapq.heappush(self.small_part, -num)
            self.small_length += 1
            if self.big_length and self.small_part[0] > self.big_part[0]:
                # 小的去大的里面呗
                self.small_length -= 1
                self.big_length += 1
                temp = -heapq.heappop(self.small_part)
                heapq.heappush(self.big_part, temp)
                if self.big_length > self.small_length + 1:
                    self.big_length -= 1
                    self.small_length += 1
                    temp = -heapq.heappop(self.big_part)
                    heapq.heappush(self.small_part, temp)
                    return 
            elif self.small_length > self.big_length + 1:
                self.small_length -= 1
                self.big_length += 1
                temp = -heapq.heappop(self.small_part)
                heapq.heappush(self.big_part, temp)
                return 
    def findMedian(self) -> float:
        # 奇数个元素：中位数是左堆堆顶
        if abs(self.big_length - self.small_length):
            return -self.small_part[0] if self.small_length > self.big_length else self.big_part[0]
        # 偶数个元素：中位数是两个堆顶的平均值
        return (self.big_part[0] - self.small_part[0]) / 2.0







import heapq

class MedianFinder:

    def __init__(self):
        # 大顶堆：存较小的一半数（用负数实现）
        self.small_part = []
        # 小顶堆：存较大的一半数
        self.big_part = []

    def addNum(self, num: int) -> None:
        # 1. 判断数字应该放入哪一堆
        if self.small_part and num <= -self.small_part[0]:
            # 数字 ≤ 左半最大值 → 放入大顶堆
            heapq.heappush(self.small_part, -num)
        else:
            # 数字 > 左半最大值 → 放入小顶堆
            heapq.heappush(self.big_part, num)

        # 2. 平衡堆大小：左堆最多比右堆多1个，右堆不能比左堆多
        if len(self.small_part) > len(self.big_part) + 1:
            # 左堆太多 → 移一个到右堆
            temp = -heapq.heappop(self.small_part)
            heapq.heappush(self.big_part, temp)
        elif len(self.big_part) > len(self.small_part):
            # 右堆太多 → 移一个到左堆
            temp = heapq.heappop(self.big_part)
            heapq.heappush(self.small_part, -temp)

    def findMedian(self) -> float:
        # 奇数个元素：左堆多一个，返回左堆堆顶（取反！）
        if len(self.small_part) > len(self.big_part):
            return -self.small_part[0]
        # 偶数个元素：两个堆顶平均值
        return (-self.small_part[0] + self.big_part[0]) / 2.0