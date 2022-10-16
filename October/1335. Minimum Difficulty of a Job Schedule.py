class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        job = len(jobDifficulty)
        
        # BASE CASES
        if d > job:
            return -1
        if d == job:
            s = 0
            for i in jobDifficulty:
                s += i
            return s
        
        #GENRAL CASE
        @cache
        def schedule(pos,remdays):
            if remdays == 0: 
                return max(jobDifficulty[pos:])
            
            curr = 0
            result = float('inf')
            
            for i in range(pos,job-remdays):
                curr = max(jobDifficulty[i],curr)
                result = min(result,curr+schedule(i+1,remdays-1))
            return result
        
        return schedule(0,d-1)
