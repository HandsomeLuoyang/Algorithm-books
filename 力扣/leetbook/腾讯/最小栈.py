class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, x: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)
        self.stack.append(x)


    def pop(self) -> None:
        if len(self.stack) > 0:
            if self.min_stack[-1] == self.stack[-1]:
                self.min_stack.pop(-1)
            self.stack.pop(-1)


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()