class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_stack.append(float('inf'))
        self.min_number = float('inf')

    def push(self, val: int) -> None:
        if val <= self.min_number:
            self.min_number = val
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        cur = self.stack.pop()
        if cur == self.min_number:
            self.min_stack.pop()
            min_cur = self.min_stack.pop()
            self.min_number = min_cur
            self.min_stack.append(min_cur)
        
    def top(self) -> int:
        cur = self.stack.pop()
        self.stack.append(cur)
        return cur

    def getMin(self) -> int:
        return self.min_number
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()