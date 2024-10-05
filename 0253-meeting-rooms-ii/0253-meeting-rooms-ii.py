class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        events = []
        for interval in intervals:
            events.append((interval[0], 1))
            events.append((interval[1],-1))
            
        rooms = 0
        res = 0
        events.sort()
        
        for event in events:
            rooms += event[1]
            res = max(res, rooms)
            
        return res
        
        