import heapq

#一个大根堆 一个小根堆
# 确保小根堆的元素 都比大根堆大
class MedianFinder:

    def __init__(self):
        self.min_heapq = []
        self.max_heapq = []
        self.min_length = 0
        self.max_length = 0

    def addNum(self, num: int) -> None:
        if self.min_length == 0:
            heapq.heappush(self.min_heapq, num)
            self.min_length += 1
        else:
            min_value = self.min_heapq[0]
            if self.max_length == 0:
                if num > min_value:
                    heapq.heappush(self.max_heapq, -min_value)
                    self.max_length += 1
                    heapq.heappop(self.min_heapq)
                    heapq.heappush(self.min_heapq, num)
                else:
                    heapq.heappush(self.max_heapq, -num)
                    self.max_length += 1
            else:
                max_value = -self.max_heapq[0]
                if num > min_value:
                    heapq.heappush(self.min_heapq, num)
                    self.min_length += 1
                    if self.min_length > self.max_length + 1:
                        value = heapq.heappop(self.min_heapq)
                        self.min_length -= 1
                        heapq.heappush(self.max_heapq, -value)
                        self.max_length += 1
                else:
                    heapq.heappush(self.max_heapq, -num)
                    self.max_length += 1
                    if self.max_length > self.min_length + 1:
                        value = -heapq.heappop(self.max_heapq)
                        self.max_length -= 1
                        heapq.heappush(self.min_heapq, value)
                        self.min_length += 1
                    
    def findMedian(self) -> float:
        if self.min_length == self.max_length:
            return (-self.max_heapq[0] + self.min_heapq[0]) / 2
        elif self.min_length > self.max_length:
            return self.min_heapq[0]
        else:
            return -self.max_heapq[0]
    
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()