class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1 = len(firstList)
        n2 = len(secondList)
        
        if n1 == 0 or n2 == 0:
            return []
        
        output = []
        i,j = 0,0
        while i < len(firstList) and j < len(secondList):
            x = max(firstList[i][0],secondList[j][0])
            y = min(firstList[i][1],secondList[j][1])
            if x <=y:
                output.append([x,y])
            if firstList[i][1]>= secondList[j][1]:
                j +=1
            else:
                i+=1   
        return output
