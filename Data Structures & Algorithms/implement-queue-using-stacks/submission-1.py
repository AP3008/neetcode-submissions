class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.isReversed = False

    def push(self, x: int) -> None:
        if self.isReversed:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            self.isReversed = False
            self.stack1.append(x)
        else:
            self.stack1.append(x)

    def pop(self) -> int:
        store = -1
        if self.isReversed:
            store = self.stack2.pop()
            for _ in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
            self.isReversed = False
        else:
            for _ in range(len(self.stack1)-1):
                self.stack2.append(self.stack1.pop())
            store = self.stack1.pop()
            self.isReversed = True
        return store 
    def peek(self) -> int:
        if self.isReversed:
            return self.stack2[-1]
        else:
            for _ in range(len(self.stack1)-1):
                self.stack2.append(self.stack1.pop())
            store = self.stack1.pop()
            self.stack2.append(store)
            self.isReversed = True
            return store 

    def empty(self) -> bool:
        return False if self.stack1 or self.stack2 else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()