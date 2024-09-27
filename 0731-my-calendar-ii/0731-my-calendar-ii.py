class MyCalendarTwo:

    def __init__(self):
        self.timeline = []
    def book(self, start: int, end: int) -> bool:
        self.timeline.append((start, 1))
        self.timeline.append((end, -1))
        
        count = 0
        for t in sorted(self.timeline):
            count += t[1]
            if count == 3:
                self.timeline.pop()
                self.timeline.pop()
                return False
            
        return True
            
            
        
            
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)