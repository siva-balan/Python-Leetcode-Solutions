class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        
        l,r = 0, n-1
        lmax,rmax = height[l],height[r]
        output = 0
        
        while l <r:
            if lmax <= rmax:
                l +=1
                lmax = max(lmax,height[l])
                output += lmax - height[l]
            else:
                r -=1
                rmax = max(rmax,height[r])
                output += rmax - height[r]
                
        return output
