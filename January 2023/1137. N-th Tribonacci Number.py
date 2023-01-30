class Solution:
    def tribonacci(self, n: int) -> int:

        """t0,t1,t2 = 0,1,1

        if n==0: return t0
        elif n==1: return t1
        elif n==2: return t2

        def tribo(n):
            if n <3:
                if n==0: return t0
                elif n==1: return t1
                elif n==2: return t2
            else:
                return tribo(n-1) + tribo(n-2) + tribo(n-3)
        return tribo(n)"""

        d = defaultdict(int)

        d[0] , d[1], d[2] = 0,1,1

        def rec(n):
            if n in d:
                return d[n]
            d[n] = rec(n-1) + rec(n-2) + rec(n-3)
            return d[n]
        return rec(n)




