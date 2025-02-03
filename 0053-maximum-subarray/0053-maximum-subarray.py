class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cursum = 0
        maxsum = 0
        maxval = float("-inf")
        for r in range(len(nums)):
            cursum = max(0, nums[r] + cursum)
            maxsum = max(maxsum, cursum)
            maxval = max(maxval, nums[r])

        if maxsum == 0:
            return maxval
        return maxsum