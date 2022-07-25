class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0,len(numbers) -1
        arr =[]
        while i<j :
            if numbers[i] + numbers[j] == target:
                arr.append(i+1)
                arr.append(j+1)
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -=1
        return arr

    
