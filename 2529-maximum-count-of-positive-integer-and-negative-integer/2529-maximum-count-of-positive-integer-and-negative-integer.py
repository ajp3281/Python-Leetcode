class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums)-1
        
        leftcount, rightcount = 0,0
        
        while left <= len(nums) - 1 and nums[left] < 0:
            leftcount += 1
            left += 1
            
        while right >= 0 and nums[right] > 0:
            rightcount += 1
            right -= 1
            
        return max(rightcount,leftcount)
            