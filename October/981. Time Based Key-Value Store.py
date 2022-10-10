class TimeMap:

    def __init__(self):
        self.map ={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map:
            self.map[key] = {}
        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""
        for i in range(timestamp,0,-1):
            if i in self.map[key]:
                return self.map[key][i]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
