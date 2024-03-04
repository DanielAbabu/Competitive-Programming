class MinStack:

    def __init__(self):
        self.stk = []
        self.minm = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.minm or val <= self.minm[-1]:
            self.minm.append(val)
        
    def pop(self) -> None:
        if self.stk.pop() == self.minm[-1]:
            self.minm.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minm[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()