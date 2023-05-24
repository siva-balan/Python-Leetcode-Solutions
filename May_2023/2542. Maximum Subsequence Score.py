class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        y = zip(nums1,nums2)
        y = sorted(y, key = lambda x : x[1],reverse = True)
        n = len(nums1)

        total,output = 0,0
        heap = []
        
        for num in y:
            n1,n2 = num

            heappush(heap,n1)
            total +=n1
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                output = max(output,total*n2)

        return output
