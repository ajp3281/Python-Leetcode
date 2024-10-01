# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # trying to find first min element
        # if case is valid, go left to keep finding min
        # else we know all previous are invalid
        left = 0 
        right = n
        
        while left < right:
            mid = (left + right) // 2
            
            if isBadVersion(mid) == True:
                right = mid
            else:
                left = mid + 1
                
        if isBadVersion(left) == True:
            return left
        return right