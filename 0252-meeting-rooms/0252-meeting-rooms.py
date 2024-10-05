class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        
        # 2,4 - 7,10
        # line sweep instead
        # add a 1 for every start, subtract 1 for every end
        # if count > 1 for any index, return False
        # 0, 30 - 5,10 - 15,20
        # hashmap[0] = 1
        # hashmap[5] = hashmap[0] + 1 etc
        # how to get count of prev meetings?
        # count before you iterate
        events = []
        for interval in intervals:
            events.append((interval[0],1))
            events.append((interval[1],-1))
        events.sort()
        meetings = 0
        for event in events:
            meetings += event[1]
            if meetings >= 2:
                return False
        return True
             
            
            
            
                
            
        