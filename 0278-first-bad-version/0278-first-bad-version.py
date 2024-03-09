# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        minimum = n
        low = 0
        high = n
        
        while low <= high:
            med = (high+low)//2
            
            if isBadVersion(med):
                minimum = min(n,med)
                
                high = med-1
                
            else:
                low = med+1
                
        return minimum
        