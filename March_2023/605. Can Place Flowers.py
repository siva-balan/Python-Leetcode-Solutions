class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)

        if m <3 and n >=2: return False
        if m ==1 and flowerbed[0] == 0:
            if n == 1 or n == 0: return True
            else: return False

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i-1 < 0 and flowerbed[i+1] == 0:
                    n -=1
                    flowerbed[i] = 1
                elif i +1 == len(flowerbed) and flowerbed[i-1] == 0:
                    n -=1
                    flowerbed[i] = 1
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    n -=1
                    flowerbed[i] = 1
        
        return n <= 0
