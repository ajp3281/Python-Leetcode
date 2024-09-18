class TimeMap:
    # build hashmap for key-val match
    # build arr to store keys
    # keep track of minimum/max seen and search through it?
    
    '''
    arr = [None, foo, None, None, foo]
    hashmap = {
        foo: [bar, bar, bar, bar, bar2]
    }
    ['high', 'high', 'high', 'high', 'high', 'high', 'high', 'high', 'high', 'high', 'high', 'high', 'high', 'high', 'high', 'high', 'high', 'high', 'high', 'high', 'low']
    
    '''
    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap[key]
        if len(values) == 0 or timestamp < values[0][0]:
            return ""
        if timestamp == values[0][0]:
            return values[0][1]
        if timestamp >= values[-1][0]:
            return values[-1][1]
        else:
            l = 0
            r = len(values)-1
            
            while l <= r:
                m = (l + r) // 2
                if values[m][0] == timestamp:
                    return values[m][1]
                if values[m][0] < timestamp:
                    l = m + 1
                else:
                    r = m - 1
        return values[l-1][1]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)