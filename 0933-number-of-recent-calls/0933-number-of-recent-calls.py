class RecentCounter:

    '''
    append 1 
    append 100 : 100 - 1 <= 3000 
    append 3001 : 3001 - 1 <= 3000
    
    '''
    def __init__(self):
        self.stack = []

    def ping(self, t: int) -> int:

        while self.stack and t - self.stack[0] > 3000:
            self.stack.pop(0)
        self.stack.append(t)
        return len(self.stack)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)