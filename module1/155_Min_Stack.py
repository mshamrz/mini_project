class MinStack:

    def __init__(self):
        self.stack = []
        self.length = 0
        self.min_val = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_val) == 0 or val <= self.min_val[-1]:
            self.min_val.append(val)
        self.length += 1

    def pop(self) -> None:
        if self.is_empty():
            raise ValueError('Stack is empty')
        self.length -= 1
        el = self.stack.pop()
        if el == self.min_val[-1]:
            self.min_val.pop()
        return el

    def top(self) -> int:
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
    def is_empty(self):
        return self.length == 0
    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
