class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        l,r = 1, min(time) * totalTrips
        """time.sort()
        while l <= r:
            m = (l+r)//2
            trip = 0
            ttime = 0
            for i in range(m+1):
                trip += time[m]//time[i]
                ttime = time[i]
            if totalTrips == trip:
                return ttime
            elif totalTrips > trip:
                l = m+1
            else:
                r = m-1
        return l"""
        while l < r:
            m = (l + r) // 2
            val = sum(m // t for t in time)
            if val >= totalTrips:
                r = m
            else:
                l = m + 1
        return l
