import random
class RandomizedSet:
    
    
    def __init__(self):
        self.a=list()
        self.ind=dict()

    def insert(self, val: int) -> bool:
        if val in self.ind.keys():
            return False
        self.a.append(val)
        self.ind[val]=len(self.a)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.ind.keys():
            # print(self.a)
            self.a[self.ind[val]],self.a[-1]=self.a[-1],self.a[self.ind[val]]
            self.ind[self.a[self.ind[val]]]=self.ind[val]
            self.ind[val]=len(self.a)-1
            
            # print(self.a)
            self.a.pop()
            self.ind.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        b=random.randint(0,len(self.a)-1)
        
        return self.a[b]
