class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        """n = len(stones)
        output = 0
        stones.sort()
        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    output += 1
                    break
        return output"""

        def remove_point(a,b):                          
            points.discard((a,b))
            for y in x_dic[a]:
                if (a,y) in points:
                    remove_point(a,y)

            for x in y_dic[b]:
                if (x,b) in points:
                    remove_point(x,b)

        x_dic = defaultdict(list)
        y_dic = defaultdict(list)
        points= {(i,j) for i,j in stones}
        
        for i,j in stones:                                
            x_dic[i].append(j)
            y_dic[j].append(i)

        cnt = 0
        for a,b in stones:                               
            if (a,b) in points:
                remove_point(a,b)
                cnt+=1

        return len(stones)-cnt
