class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        cursum = nums[0]
        maxsum = nums[0]
        for r in range(1, len(nums)):
            if nums[r] > nums[r-1]:
                cursum += nums[r]
            else:
                cursum = nums[r]

            maxsum = max(maxsum, cursum)

        return maxsum