class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        last_min = self.mini[-1] if len(self.mini) !=0 else val
        self.mini.append(min(last_min, val))

    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.stack[-1] if len(self.stack) != 0 else None

    def getMin(self) -> int:
        return self.mini[-1]
        
