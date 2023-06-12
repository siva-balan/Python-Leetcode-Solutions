class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        output = []
        if len(nums) == 0: return  []
        elif len(nums) == 1 : return [str(nums[0])]
        l,r = nums[0],nums[0]
        for i in range(len(nums)):
            if i == len(nums)-1:
                r = nums[i]
                if l == r:
                    output.append(str(l))
                else:
                    x = str(l) + "->" + str(r)
                    output.append(x)
                break
            if nums[i+1] == nums[i]+1:
                r = nums[i+1]
            else:
                if l == r:
                    output.append(str(l))
                    l = nums[i+1]
                    r = nums[i+1]
                else:
                    x = str(l) + "->" + str(r)
                    output.append(x)
                    l = nums[i+1]
                    r = nums[i+1]
        
        return output

