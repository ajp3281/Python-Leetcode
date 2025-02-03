class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # sliding window
        # increment right if we are at sum less than target
        # increment left if we are over
        
        l = 0
        cur = 0
        minlen = float("inf")
        for r in range(len(nums)):

            if cur < target:
                cur += nums[r]

            while cur >= target:
                minlen = min(minlen, r - l + 1)
                cur -= nums[l]
                l += 1

        if minlen == float("inf"):
            return 0
        return minlen

            

