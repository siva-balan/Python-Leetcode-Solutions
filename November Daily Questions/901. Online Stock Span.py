class StockSpanner:

    def __init__(self):
        self.stack=[(0,0)]

    def next(self, price: int) -> int:
        s=self.stack
        
        last,lastDays=s.pop()
        
        days=1
        while price>=last and s:
                days+=lastDays
                last,lastDays=s.pop()
                
        else:
            s.append((last,lastDays))
        s.append((price,days))
        return days 


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
