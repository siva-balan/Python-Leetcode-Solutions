from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        val = collections.defaultdict(list)
        for l,r,h in buildings:
            val[l].append([-1,h])
            val[r].append([1,h])
            
        sl =SortedList()
        sl.add(0)
        
        output = []
        last_height = 0
        for i in sorted(val.keys()):
            for f, h in val[i]:
                if f == -1:
                    sl.add(h)
                else:
                    sl.remove(h)
            curr_height = sl[-1]
            if curr_height != last_height:
                output.append([i,curr_height])
            last_height = curr_height
        return output
