class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        # looks like prefix arr problem?

        # ex: 10 14 6 13

        # if prefix[i] > prefix[-1] - prefix[i], res += 1

        # 0,10,4
        # 10,4,-8,7
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1] + nums[i])


        res = 0
        for i in range(len(nums)-1):
            if prefix[i] >= (prefix[-1] - prefix[i]):
                res += 1
        return res
        