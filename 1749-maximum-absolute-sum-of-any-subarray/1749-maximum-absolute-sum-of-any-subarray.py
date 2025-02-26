class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # go either as negative or positive as possible
        # can't do sliding window can we?
        # prefix? 
        # we can do 2x loop sliding window
        l = 0
        mostmax = 0
        current = 0
        for r in range(len(nums)):
            current += nums[r]

            if current < 0:
                current = 0

            mostmax = max(mostmax, current)

        mostmin = 0
        current = 0
        mostmin = float("inf")
        for r in range(len(nums)):
            current += nums[r]

            if current > 0:
                current = 0

            mostmin = min(mostmin, current)
        
        return max(abs(mostmin), abs(mostmax))