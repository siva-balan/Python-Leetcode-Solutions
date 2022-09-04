class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        m = min(height[l],height[r])
        water = (r-l)*m
        while l<r:
            if height[l]> height[r]:
                r -=1
                water = max(water,(r-l)*min(height[l],height[r]))
            else:
                l +=1
                water = max(water,(r-l)*min(height[l],height[r]))
        return water
