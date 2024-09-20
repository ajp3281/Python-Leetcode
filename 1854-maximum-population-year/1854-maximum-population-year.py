from sortedcontainers import SortedDict
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        hashmap = SortedDict()
        
        for log in logs:
            if log[0] in hashmap:
                hashmap[log[0]] += 1
            else:
                hashmap[log[0]] = 1
            
            if log[1] in hashmap:
                hashmap[log[1]] -= 1
            else:
                hashmap[log[1]] = -1
                
        current = 0
        maxval = 0
        res = 0
        for time in hashmap.keys():
            current += hashmap[time]
            if current > maxval:
                maxval = current
                res = time
                
            
        return res
        