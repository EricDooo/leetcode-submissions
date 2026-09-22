class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minval = val
        else:
            self.stack.append(val - self.minval)
            if val < self.minval:
                self.minval = val


    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        # pop is negative, meaning a min change happened here
        # we basically add back the popped value to retrieve the old min back
        if pop < 0:
            self.minval = self.minval - pop
        

    def top(self) -> int:
        top = self.stack[-1]
        # if top is > 0 then the minval has been changed
        if top > 0:
            return top + self.minval
        else:
            return self.minval
        

    def getMin(self) -> int:
        return self.minval
        
