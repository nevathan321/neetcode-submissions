class MinStack:

    def __init__(self):
        self.Stack = []

    def push(self, val: int) -> None:
        self.Stack.append(val)

    def pop(self) -> None:
        self.Stack.pop()

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        min_val = float('inf')
        for num in self.Stack:
            if num < min_val:
                min_val = num
        return min_val



        

    
































