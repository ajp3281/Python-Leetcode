class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # solution is either total - min sum
        # or maxsubarray sum

        cursum = float("-inf")
        curminsum = float("inf")
        maxsum = float("-inf")
        minsum = float("inf")
        totalsum = 0

        for r in range(len(nums)):
            cursum = max(nums[r], cursum + nums[r])
            curminsum = min(nums[r], curminsum + nums[r])
            maxsum = max(maxsum, cursum)
            minsum = min(minsum, curminsum)
            totalsum += nums[r]
            print(curminsum, minsum)

        print(maxsum, minsum, totalsum)
        if minsum == totalsum:
            return maxsum
        
        # 3 - -5
        return max(totalsum - minsum, maxsum)