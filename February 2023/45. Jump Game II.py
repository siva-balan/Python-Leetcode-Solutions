class Solution:
    def jump(self, nums: List[int]) -> int:

        """output = [float("inf")]
        n = len(nums)
        def steps(i,output,step):
            if step >= output[0]:
                return
            if i == n-1:
                output[0] = min(output[0],step)
            elif i >=n:
                return
            else:
                for k in range(1,nums[i]+1):
                    steps(i+k,output,step+1)
        
        steps(0,output,0)
        return output[0]"""

        memo={}
        def rec_dp(curr_pos):
            if curr_pos>=len(nums)-1:
                return 0
            if curr_pos in memo:
                return memo[curr_pos]
            
            temp=float("inf")
            for i in range(1,nums[curr_pos]+1):
                temp=min(temp, 1+rec_dp(curr_pos+i))
            
            memo[curr_pos]=temp
            return temp
        
        return rec_dp(0)
