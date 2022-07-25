class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x=0
        for i in range(0,len(nums1)):
            if x>=n:
                break
            if nums1[i]==0:
                nums1[i]=nums2[x]
                x+=1
        nums1.sort()
                    
