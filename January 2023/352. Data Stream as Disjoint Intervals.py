class SummaryRanges:

    def __init__(self):
        self.array =  set()
    def addNum(self, value: int) -> None:
        self.array.add(value)

    def getIntervals(self) -> List[List[int]]:
        out = []
        seen = set()
        
        for i in self.array:
            if i in seen:
                continue
            l,r = i,i
            while l - 1 in self.array:
                seen.add(l-1)
                l -=1
            while r +1 in self.array:
                seen.add(r+1)
                r +=1
            
            if [l,r] not in out:
                out.append([l,r])
        
        return sorted(out)




# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
