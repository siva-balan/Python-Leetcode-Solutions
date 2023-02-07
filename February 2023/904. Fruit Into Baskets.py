#Contains both O(N^2) and O(N) Solution

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        """output = 0
        for i in range(len(fruits)):
            arr = [fruits[i]]
            currmax = 1
            for j in range(i+1,len(fruits)):
                if fruits[j] in arr or len(arr) <2:
                    currmax +=1
                    if fruits[j] not in arr:
                        arr.append(fruits[j])
                else:
                    break
            output = max(output,currmax)
        return output"""

        d = defaultdict(int)
        l = 0
        output,currmax = 0,0
        i = 0
        while i < len(fruits):
            if len(d.keys()) <2 or fruits[i] in d:
                if fruits[i] not in d:
                    d[fruits[i]] = 1
                else: 
                    d[fruits[i]] +=1
                currmax +=1
            else:
                d[fruits[l]] -=1
                if d[fruits[l]] == 0:
                    d.pop(fruits[l])
                l +=1
                currmax -=1
                i -=1
            i+=1
            output = max(output,currmax)
        
        return output
