class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        increasing = 0
        decreasing = 0

        curr = 1
        for r in range(1, len(nums)):
            if nums[r] > nums[r-1]:
                curr += 1
            else:
                curr = 1
            increasing = max(increasing, curr)

        curr = 1
        for r in range(1, len(nums)):
            if nums[r] < nums[r-1]:
                curr += 1
            else:
                curr = 1
            print(curr)
            decreasing = max(decreasing, curr)
            
        print(increasing, decreasing)
        return max(increasing, decreasing)

        