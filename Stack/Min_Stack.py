class MinStack:

    def __init__(self):
        self.mstack = []
        

    def push(self, val: int) -> None:
        self.mstack.append(val)


    def pop(self) -> None:
        last = self.mstack[-1]
        self.mstack.pop(-1)
        return last

    def top(self) -> int:            
        return self.mstack[-1]

        

    def getMin(self) -> int:
        return min(self.mstack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()