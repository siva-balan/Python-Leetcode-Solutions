class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key = lambda x : (x[0],x[1]))
        print(points)
        output = 1
        minx = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= minx:
                minx = min(minx, points[i][1])
            else:
                output += 1
                minx = points[i][1]
        
        """while i <= len(points)-1:
            for j in range(i+1,len(points)):
                if points[j][0] <= points[i][1] and j != len(points)-1:
                    continue
                elif points[j][0] <= points[i][1] and j == len(points)-1:
                    output +=1
                    i = j
                else:
                    output +=1
                    i = j
                    break
            i = j"""

        return output
