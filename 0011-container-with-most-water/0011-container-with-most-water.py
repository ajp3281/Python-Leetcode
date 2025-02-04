class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # ptrs starting from left and right side
        # decrement whichever val is less
        # iterate while l < r
        # record maxarea at every iteration

        l = 0
        r = len(height) - 1
        maxarea = 0 
        while l < r:

            area = min(height[l],height[r]) * (r - l)
            maxarea = max(area, maxarea)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return maxarea


