class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        span = 0
        tmp = self.stack[:]
        while tmp and tmp[-1] <= price:
            span+=1 
            tmp.pop()
        return span 
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)