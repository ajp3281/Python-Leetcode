class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # run thru array once and multiply prefixes
        # run thru array again and multiply suffixes
        # combine and store res
        
        #  1        
        #  24    12    4   1
        res = [None] * len(nums)
        product_so_far = 1
        for i in range(len(nums)):
            res[i] = product_so_far
            product_so_far *= nums[i]
        
        product_so_far = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= product_so_far
            product_so_far *= nums[i]
        
        return res
            
        
        
        