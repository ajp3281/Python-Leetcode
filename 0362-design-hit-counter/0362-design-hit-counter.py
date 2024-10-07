class HitCounter:

    def __init__(self):
        # use a queue, pop everything thats 300 + seconds away from current timestamp
        self.q = deque([])

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.q and self.q[0] + 300 <= timestamp:
            self.q.popleft()
        return len(self.q)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)