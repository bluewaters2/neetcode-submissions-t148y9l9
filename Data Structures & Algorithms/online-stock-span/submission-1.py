# there are 2 cases, 1 where the price is less than or equal to the top of the stack which case we pop 
# and add the cnt and if price is greater than current price then we just append the curr price

class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cnt = 1
        
        while self.stack and self.stack[-1][0] <= price:
            p, c = self.stack.pop()
            cnt += c
        
        self.stack.append((price, cnt))
        return cnt


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)