class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #  check if its left val is greater than right max - if it is insert at back
        # if left val is less than right val and right val is greater than right val - replace right
        # 
        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]
        
        for interval in intervals:
            if interval[0] > res[-1][1]:
                res.append(interval)
            elif interval[0] >= res[-1][0]:
                res[-1][1] = max(interval[1],res[-1][1])
        
        return res
            
            
        