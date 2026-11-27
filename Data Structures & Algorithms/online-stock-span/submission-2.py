class StockSpanner:

    def __init__(self):
        # [price, days it was bigger]
        self.stack = [] 


    def next(self, price: int) -> int:
        span = 1 
        while self.stack and price >= self.stack[-1][0]:
            p, s = self.stack.pop()
            span+=s
        self.stack.append((price, span))
        return span 
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)