class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        a = []
        b = []
        
        n = len(img1)
        
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    a.append((i,j))
                if img2[i][j] == 1:
                    b.append((i,j))
        
        d = {}
        
        for x1,y1 in a:
            for x2,y2 in b:
                shift = (x2-x1,y2-y1)
                if shift in d:
                    d[shift] +=1
                else:
                    d[shift] = 1
        
        return max(d.values()) if len(d.values()) > 0 else 0
