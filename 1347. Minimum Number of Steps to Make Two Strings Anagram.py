class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        ds = defaultdict(int)
        dt = defaultdict(int)
        for i in s:
            ds[i] +=1
        for j in t:
            dt[j] +=1
        for i in s:
            if i not in dt:
                dt[i] = 0
        for i in t:
            if i not in ds:
                ds[i] = 0
        out = 0
        for key,value in dt.items():
            x = value - ds[key]
            out += abs(x)
        return int(out/2)
