# naive solution, is just creating a stack, but we want to keep the minimum value in O(1) time. So we can have a regular stack but we want each element to be an array store the value at 0 index, and in 1 stores the minimum element of the list including it, but not anything that follows it. This works because we never search the entire list, we just pop, so remembering the min from previous attempts to store. 
class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        if val < self.minVal: 
            self.minVal = val 
        self.stack.append([val, self.minVal])

    def pop(self) -> None:
        self.stack.pop()
        self.minVal = self.stack[-1][1] if self.stack else float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
