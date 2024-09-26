class MyCalendar:

    def __init__(self):
        self.bookings = []

        # ["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
#[[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
# 47,50 -> 33,50 -> 
# make arr of intervals 
    def book(self, start: int, end: int) -> bool:
        if not self.bookings:
            self.bookings.append((start, end))
            return True
        
        #sorted_intervals = sorted(self.bookings)
        for interval in self.bookings:
            if (start >= interval[0] and start < interval[1]) or (end > interval[0] and end <= interval[1]) or (start < interval[0] and end > interval[1]):
                return False
        
        self.bookings.append((start, end))
        return True
            
        
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)