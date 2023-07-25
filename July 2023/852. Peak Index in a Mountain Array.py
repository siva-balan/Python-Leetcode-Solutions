class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        output = 0
        for i in range(1,len(arr)):
            # if arr[i] > arr[i-1]:
            #     continue
            if arr[i]> arr[i-1] and (arr[i] > arr[i+1]):
                output = i
            # elif arr[i] > arr[i+1] and output != 0:
            #     continue
        return output
