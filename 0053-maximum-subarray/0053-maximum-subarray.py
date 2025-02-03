class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cursum = nums[0]
        maxsum = nums[0]

        for r in range(1,len(nums)):
            cursum = max(nums[r], nums[r] + cursum)
            maxsum = max(maxsum, cursum)

        return maxsum