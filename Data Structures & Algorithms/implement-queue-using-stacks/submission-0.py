class MyQueue:
    # Same idea but we can only pop from the right so we are going to use two stacks. 
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        # We need to pop from the left, so we can pop all of the values into a tmp list which will then give us all of the values in reverse order. Which we iterate through it again and apply 
        tmp = []
        while self.stack:
            tmp.append(self.stack.pop())
        
        for i in range(len(tmp)-2, -1,-1):
            self.stack.append(tmp[i])
        return tmp[-1]

    def peek(self) -> int:
        # return self.stack[0]
        tmp = []
        while self.stack:
            tmp.append(self.stack.pop())
        for i in range(len(tmp)-1, -1, -1):
            self.stack.append(tmp[i])
        return tmp[-1]

    def empty(self) -> bool:
        return False if self.stack else True 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()