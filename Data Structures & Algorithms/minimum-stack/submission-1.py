class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
            self.stack.append(0)
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        else:
            pop = self.stack.pop()
            if pop < 0:
                self.min = self.min - pop
        

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min
        

    def getMin(self) -> int:
        return self.min
        
