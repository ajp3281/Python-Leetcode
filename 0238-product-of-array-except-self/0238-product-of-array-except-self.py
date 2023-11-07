class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # run thru array once and multiply prefixes
        # run thru array again and multiply suffixes
        # combine and store res
        
        #  1        
        #  24    12    4   1
        prefix = [1 for _ in range(len(nums))]
        for index in range(1,len(nums)):
            prefix[index] = prefix[index-1] * nums[index-1]
        suffix = [1 for _ in range(len(nums))]
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            prefix[i] *= suffix[i]
        
        return prefix
        
        