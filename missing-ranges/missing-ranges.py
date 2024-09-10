class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        '''
        Input: nums = [0,1,3,50,75], lower = 0, upper = 99
        Output: [[2,2],[4,49],[51,74],[76,99]
        
        # push range from nums[index] to nums[index+1] 
        # merge after?
        
        '''
         
        res = []
        if len(nums) == 0 or nums[0] > lower:
            res.append([lower, nums[0] - 1] if nums else [lower, upper])
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                continue
            else:
                res.append([nums[i]+1, nums[i+1]-1])
        if len(nums) > 0 and nums[-1] < upper:
            res.append([nums[-1]+1, upper])
        return res