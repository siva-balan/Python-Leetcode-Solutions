class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s =set()
        output = []
        for z in range(len(nums)):
            x = z + 1
            y = len(nums)-1
            while x < y:
                if nums[x] + nums[y] + nums[z] == 0:
                    i = [nums[x],nums[y],nums[z]]
                    i.sort()
                    if tuple(i) not in s:
                        s.add(tuple(i))
                        output.append([nums[x],nums[y],nums[z]])
                    x +=1
                elif nums[x] + nums[y] + nums[z] > 0:
                    y -=1
                else:
                    x +=1
    
        return output
