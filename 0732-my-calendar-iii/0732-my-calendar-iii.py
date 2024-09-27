class MyCalendarThree:

    def __init__(self):
        self.timeline = []

    def book(self, startTime: int, endTime: int) -> int:
        self.timeline.append((startTime, 1))
        self.timeline.append((endTime, -1))
        
        max_count = 0
        count = 0
        for t in sorted(self.timeline):
            count += t[1]
            max_count = max(count, max_count)
            
        return max_count
            
        
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)