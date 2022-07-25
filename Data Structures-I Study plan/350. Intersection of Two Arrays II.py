class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1,nums2 = nums2, nums1
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        result = []
        while j <len(nums2) and i <len(nums1):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                j +=1
                i +=1
            elif nums1[i] < nums2[j]:
                i +=1
            else:
                j +=1
        return result
