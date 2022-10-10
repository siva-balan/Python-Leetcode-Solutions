from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.d[start] = self.d.get(start,0) +1
        self.d[end] = self.d.get(end,0) -1
        
        curr = output = 0
        
        for i in self.d.values():
            curr += i
            output = max(curr,output)
        return output


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
