class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        time = 0
        ans = []
        T = 0

        for t in range(len(tasks)):
            tasks[t].append(t)
            
        tasks.sort(key=lambda x: (x[0], x[1], x[2]))
        s,p,i = tasks[T]
        T+=1
        Q = [(p,i,s)]

        while Q or T < len(tasks): 
            while not Q or (T < len(tasks) and tasks[T][0] <= time): 
                s,p,i = tasks[T]
                T += 1
                heapq.heappush(Q, (p,i,s))
            
            pn, inn, sn = heapq.heappop(Q)
            ans.append(inn)
            time = max(time,sn) + pn

        return ans
