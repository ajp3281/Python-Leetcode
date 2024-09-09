class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # two pointer approach - one for each endpoint
        # start from right and left, whichever is less, decrement value
        # at every iteration calculate val and see if its greater than max
        
        
        l = 0
        r = len(height)-1
        res = 0
        
        while l < r:
            
            currentarea = min(height[r], height[l]) * (r - l)
            res = max(res, currentarea)
            
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
                
        return res
            
        