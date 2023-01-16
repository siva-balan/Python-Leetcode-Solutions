class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        """if len(intervals) == 0:
            return [newInterval]
        output = []
        x,i = 0,0
        if newInterval[0] > intervals[len(intervals)-1][1]:
            output = intervals
            output.append(newInterval)
            return output

        while i < len(intervals):
            if newInterval[0] <= intervals[i][1] and x == 0:
                if i == len(intervals)-1:
                    output.append([min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])])
                    return output
                
                for j in range(i+1,len(intervals)):
                    if newInterval[1] < intervals[j][0]:
                        output.append([intervals[i][0],max(intervals[j-1][1],newInterval[1])])
                        x += 1
                        i = j-1
            else:
                output.append(intervals[i])
            i +=1
        return output"""

        result = []
        
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        
        result.append(newInterval); 
        return result
