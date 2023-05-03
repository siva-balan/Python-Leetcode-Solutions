class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        output = []
        x,y = [], []

        for i in nums1:
            if i not in nums2 and i not in x:
                x.append(i)
        output.append(x)

        for j in nums2:
            if j not in nums1 and j not in y:
                y.append(j)
        output.append(y)
        return output
