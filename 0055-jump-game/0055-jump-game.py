class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        
        cur_dist = 0
        max_dist = 0
        
        for r in range(len(nums)):
            max_dist = max(max_dist, r + nums[r])
            if max_dist >= target:
                return True
            if max_dist <= r:
                return False
            
        
        return False
        