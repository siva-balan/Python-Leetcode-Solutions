# SOLUTION FROM LEETCODE DISCUSS

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 1
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict() 
        ## usage[f][k]=v : frequency = f, key = k, v = value 
        self.usage = defaultdict(OrderedDict)
        ## current least frequenct usage
        self.LF = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        ## update the frequency
        self.update(node, node.val)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key not in self.cache: 
            if len(self.cache) >= self.capacity:
                ## pop the node with current least freuenct usage (FIFO)
                k, v = self.usage[self.LF].popitem(last=False)
                self.cache.pop(k)
            node = ListNode(key, value)
            ## save the new node into cache and usage map
            self.cache[key] = node
            self.usage[1][key] = value
            ## reset current LF to 1
            self.LF = 1
        else: 
            ## update the vaLue of existing key 
            node = self.cache[key]
            node.val = value
            ## update the frequency
            self.update(node, value)
            
            
    def update(self, node, newVal):
        k, f = node.key, node.freq
        ## delete from the former frequency (f)
        self.usage[f].pop(k)
        ## if the former frequency is the LFU and it become empty
        ## the new frequency (f+1) become new LFU
        if not self.usage[f] and self.LF == f:
            self.LF += 1
        ## push to the new frequency (f+1)
        self.usage[f+1][k] = newVal
        node.freq += 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
