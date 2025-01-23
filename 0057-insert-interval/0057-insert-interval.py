class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # build res arr
        # if interval[i][1] > newinterval[0] - there is overlap

        # iterate until newinterval[1] < interval[i][0] 
        # if there is overlap newinterval[1] =  max(interval[i][1], newinterval[1])

        res = []
        i = 0
        if not intervals:
            return [newInterval]
            
        inserted = False
        while i < len(intervals):
            if newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][0]:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                i += 1
                while i < len(intervals) and newInterval[1] >= intervals[i][0]:
                    newInterval[1] = max(newInterval[1], intervals[i][1])
                    i += 1
                res.append(newInterval)
                inserted=True
            else:
                res.append(intervals[i])
                i += 1
            
        if not inserted:
            res.append(newInterval)

        res.sort()
        return res
        