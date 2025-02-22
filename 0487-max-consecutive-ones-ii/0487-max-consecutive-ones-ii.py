class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        # longest streak of 1s with 1 zero
        l = 0
        r = 0
        count = 0
        res = 0
        prev_seen_zero = None
        while r < len(nums):
            if nums[r] == 1:
                r += 1
            elif nums[r] == 0 and count == 0:
                r += 1
                count += 1
                prev_seen_zero = r
            else:
                while r < len(nums) and nums[r] == 0:
                    r += 1
                l = r = prev_seen_zero
                count = 0
            res = max(res, r - l )
        
        return res
        