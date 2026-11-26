class MyStack:
    # Since we need O(1) push, O(1) pop and every other operation O(1). Even though in python we can use append and pop. We do not want to use that as it trivaializes the problem. 
    # We are only allowed to use append(), q[0] (peek), q.popleft() 
    # Okay it's impossible to implement this in O(1) times using queues so then this makes it easier. 
    # For push we can append the same way O(1)
    # To pop() we can popleft() until the length of the array -1 times, and pop one last time but not pushing that back onto the q. 
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        n = len(self.q)
        for _ in range(n-1):
            self.q.append(self.q.popleft())
        return self.q.popleft() 
    def top(self) -> int:
        n = len(self.q)
        for _ in range(n-1):
            self.q.append(self.q.popleft())
        store = self.q[0]
        self.q.append(self.q.popleft())
        return store 

    def empty(self) -> bool:
        return False if self.q else True 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()