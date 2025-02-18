class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        
        # continue to remove first elem?
        # 3, -5, -2, 6
        # 3, -2, -4, 2
        # 3, 8
        # stack approach?
        # reverse prefix?
        #4,2,-1,4
        prefix = [0]
        ops = 0
        for i, num in enumerate(nums):
            prefix.append(prefix[-1] + nums[i])

            if prefix[-1] < 0:
                prefix[-1] += -nums[i]
                ops += 1
            elif i < len(nums)-1 and prefix[-1] == 0 and nums[i+1] < 0:
                prefix[-1] += max(-nums[i], -nums[i+1])
                ops += 1
        return ops