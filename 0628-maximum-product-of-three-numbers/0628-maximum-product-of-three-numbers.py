class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        firstmax = secondmax = thirdmax = float("-inf")
        
        for num in nums:
            if num > firstmax:
                thirdmax = secondmax
                secondmax = firstmax
                firstmax = num
            elif num > secondmax:
                thirdmax = secondmax
                secondmax = num
            elif num > thirdmax:
                thirdmax = num
        
        
        firstmin = float("inf")
        secondmin = float("inf")
        for num in nums:
            if num < firstmin:
                secondmin = firstmin
                firstmin = num
            elif num < secondmin:
                secondmin = num
                
        return max(firstmax*secondmax*thirdmax, firstmax*firstmin*secondmin)
        
        
            
            
                